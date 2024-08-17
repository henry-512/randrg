import requests
from bs4 import BeautifulSoup
import json
import time

# Scrapes karl.gg and retrieves all current builds in a .json format

chrToNum = {
    'A': 1,
    'B': 2,
    'C': 3,
}

weaponIdToKey = [
    'primary',
    'secondary',
]
equipIdToKey = [
    'mobility',
    'utility',
    'armor',
    'pickaxe',
]

# ['Driller', 'Engineer', 'Gunner', 'Scout']
# class 0:pri/1:sec index name
karlWeaponToDict = {
    1: [1, 0, 0, 'Warthog'],
    2: [1, 0, 1, 'Stubby'],
    3: [1, 1, 0, 'PGL'],
    4: [1, 1, 1, 'Breach'],
    5: [3, 0, 0, 'GK2'],
    6: [3, 0, 1, 'M1000'],
    7: [3, 1, 0, 'Boomstick'],
    8: [3, 1, 1, 'Zhukov'],
    9: [0, 0, 0, 'Flame'],
    10: [0, 0, 1, 'Cryo'],
    11: [0, 1, 0, 'Subata'],
    12: [0, 1, 1, 'EPC'],
    13: [2, 0, 0, 'Minigun'],
    14: [2, 0, 1, 'Thunderhead'],
    15: [2, 1, 0, 'Bulldog'],
    16: [2, 1, 1, 'BRT'],
    17: [1, 0, 2, 'LOKI'],
    18: [3, 0, 2, 'DRAK'],
    19: [0, 0, 2, 'Sludge'],
    20: [2, 0, 2, 'Hurricane'],
    21: [0, 1, 2, 'Cooker'],
    22: [1, 1, 2, 'Shard'],
    23: [2, 1, 2, 'Coilgun'],
    24: [3, 1, 2, 'Boltshark'],
}

# ['Driller', 'Engineer', 'Gunner', 'Scout']
# class 0:mobility/1:utility/2:armor name/3:pickaxe
karlEquipToDict = {
    1: [0, 0, 'Drills'],
    2: [0, 1, 'C4'],
    3: [1, 0, 'Platform'],
    4: [1, 1, 'Turret'],
    5: [2, 0, 'Zipline'],
    6: [2, 1, 'Shield'],
    7: [3, 0, 'Grapple'],
    8: [3, 1, 'Flare'],

    9: [1, 2, 'Engi armor'],
    10: [3, 2, 'Scout armor'],
    11: [0, 2, 'Driller armor'],
    12: [2, 2, 'Gunner armor'],

    13: [0, 3, 'Driller Pickaxe'],
    14: [1, 3, 'Engi Pickaxe'],
    15: [2, 3, 'Gunner Pickaxe'],
    16: [3, 3, 'Scout Pickaxe'],
}

# Class codes
karlClassToDict = {
    # Engineer
    1: 1,
    # Scout
    2: 3,
    # Driller
    3: 0,
    # Gunner
    4: 2,
}
drillerCode = 3
engiCode = 1
gunnerCode = 4
scoutCode = 2

# Karl url for browsing
baseUrl = 'http://karl.gg/browse?isCurrentPatch=1&sort=updated_at&direction=asc'

def addCharacter(url, *args):
    for c in args:
        url = f'{url}&characters%5B%5D={c}'
    return url

def addPage(url, page):
    return f'{url}&page={page}'

allBuilds = {
    0: [],
    1: [],
    2: [],
    3: [],
}

r = requests.get(baseUrl)
soup = BeautifulSoup(r.content, 'html.parser')

while 1:
    for a in soup.find_all('a', href=True):
        link = a['href']
        if not link.__contains__('preview'):
            continue
        print(link)

        def ld(l):
            req = requests.get(link)
            preq = BeautifulSoup(req.content, 'html.parser')
            # Preview data
            preview = preq.find('loadout-preview-page')

            # Preview tags: :loadout-data :primary :primary-mods :secondary :secondary-mods :available-equipment :equipment-mods
            return json.loads(preview[':loadout-data'])
            # return preview[':loadout-data']
        # keys
        # 'id', 'name', 'description', 'user_id', 'character_id', 'created_at',
        # 'updated_at', 'patch_id', 'throwable_id', 'mods', 'equipment_mods', 'overclocks', 'character', 'creator'
        loadout = ld(link)

        # print(loadout)
        # print(loadout['overclocks'])
        # exit(0)

        # print('character::')
        # print(loadout['character_id'])
        # karl.gg doesn't store grenades
        # print('grenade::')
        # print(loadout['throwable_id'])

        build = {
            'id': loadout['id'],
            'class': karlClassToDict[loadout['character_id']],
            'url': link,
            'primary': {},
            'secondary': {},
            'mobility': {},
            'utility': {},
            'armor': {},
            'pickaxe': {},
        }

        # print('overclocks::')
        for oc in loadout['overclocks']:
            # print(f"{oc['character_id']} {oc['gun_id']} {oc['overclock_name']}")
            weaponData = karlWeaponToDict[oc['gun_id']]
            key = weaponIdToKey[weaponData[1]]

            build[key]['oc'] = oc['overclock_name']
            build[key]['name'] = weaponData[3]
            build[key]['index'] = weaponData[2]
        
        # print('upgrades::')
        for mod in loadout['mods']:
            # print(f"{mod['id']} {mod['character_id']} {mod['gun_id']} {mod['mod_tier']}:{mod['mod_index']} {mod['mod_name']}")
            weaponData = karlWeaponToDict[mod['gun_id']]
            key = weaponIdToKey[weaponData[1]]

            build[key][mod['mod_tier']] = chrToNum[mod['mod_index']]
            build[key]['name'] = weaponData[3]
            build[key]['index'] = weaponData[2]
        
        # print('equipment::')
        for mod in loadout['equipment_mods']:
            # print(f"{mod['id']} {mod['character_id']} {mod['equipment_id']} {mod['mod_tier']}:{mod['mod_index']} {mod['mod_name']}")

            if mod['equipment_id'] not in karlEquipToDict:
                print(loadout)

            equipData = karlEquipToDict[mod['equipment_id']]
            key = equipIdToKey[equipData[1]]
            
            build[key][mod['mod_tier']] = chrToNum[mod['mod_index']]
            build[key]['name'] = equipData[2]

        # grenade
        build['grenade'] = loadout['throwable_id']

        # allBuilds[karlClassToDict[build['class']]].append(build)
        allBuilds[build['class']].append(build)
        with open('raw.txt', 'a') as f:
            f.write(f'{json.dumps(build)},\n')
        # print(build)
        time.sleep(5)

    nextButton = soup.find('a', {'aria-label':"Next &raquo;"})
    if not nextButton:
        break
    print(nextButton['href'])
    soup = BeautifulSoup(requests.get(nextButton['href']).content, 'html.parser')

# print(allBuilds)

