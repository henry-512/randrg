import json

classNames = ['Driller', 'Engineer', 'Gunner', 'Scout']
primaryNames = [['Flame', 'Cryo', 'Sludge'],
    ['Warthog', 'Stubby', 'LOKI'],
    ['Minigun', 'Auto', 'Hurricane'],
    ['GK2', 'M1000', 'DRAK']]
secondaryNames = [['Subata', 'EPC', 'Cooker'],
    ['PGL', 'Breach', 'Shard'],
    ['Bulldog', 'BRT', 'Coilgun'],
    ['Boomstick', 'Zhukov', 'Boltshark']]

def maxIndex(ar):
    return ar.index(max(ar))

def findMostMeta(parsed, cls):
    data = parsed[cls]
    build = {}

    def findMetaBuild(isPrimary):
        key = 'primary' if isPrimary else 'secondary'
        weaponData = data[key]
        weaponIndex = weaponData.index(max(
            weaponData,
            key=lambda k: k['count']
        ))

        b = {
            'mods': [],
            'mod': 0,
            'index': weaponIndex,
            'oc': max(
                weaponData[weaponIndex]['oc'],
                key=weaponData[weaponIndex]['oc'].get,
            ),
        }

        # set mods
        for i in range(5):
            digit = maxIndex(weaponData[weaponIndex]['mods'][i])
            b['mods'].append(digit)
            b['mod'] *= 10
            b['mod'] += digit + 1

        # set display name
        names = primaryNames if key == 'primary' else secondaryNames
        b['name'] = names[cls][weaponIndex]

        build[key] = b

    findMetaBuild(True)
    findMetaBuild(False)

    def findMetaEquipment(key):
        build[key] = 0
        for ar in data[key]:
            build[key] *= 10
            build[key] += maxIndex(ar) + 1

    findMetaEquipment('mobility')
    findMetaEquipment('utility')
    findMetaEquipment('armor')

    return build

def calculateMeta(mod_list):
    meta_data = []

    for mod in mod_list:
        meta_data.append(calculateSingleMeta(mod))

    return meta_data

def calculateSingleMeta(mod):
    total = sum(mod)
    mod_percent = [m / total for m in mod]
    best_percent = max(mod_percent)
    scalar = 1 / best_percent
    return [m * scalar for m in mod_percent]

def calculateOCMeta(oc_list: dict):
    total = sum(oc_list.values())
    oc_percent = {name: count / total for name,count in oc_list.items()}
    best_percent = max(oc_percent.values())
    scalar = 1 / best_percent

    return {name: percent * scalar for name,percent in oc_percent.items()}

with open('parsed.json') as f:
    parsed = json.load(f)

    # Most meta finder
    for c in range(4):
        build = findMostMeta(parsed, c)
        # print(classNames[c])
        # print(build)

    metaTable = [{
        'primary':{},
        'secondary':{},
    } for _ in range(4)]

    for classId, classData in enumerate(parsed):
        for k in ('primary', 'secondary'):
            metaTable[classId][k]['mod'] = [
                calculateMeta(data['mods'])
                for data in classData[k]
            ]
            metaTable[classId][k]['oc'] = [
                calculateOCMeta(data['oc'])
                for data in classData[k]
            ]
        
        for k in ('mobility', 'utility', 'armor', 'pickaxe'):
            metaTable[classId][k] = calculateMeta(classData[k])
        metaTable[classId]['grenade'] = calculateSingleMeta(classData['grenade'])

    with open('meta.json', 'w') as f:
        json.dump(metaTable, f, indent=2)

