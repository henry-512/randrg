import json

# DATA
primaryOC = [[
        ['Lighter Tanks', 'Sticky Additive', 'Compact Feed Valves', 'Fuel Stream Diffuser', 'Face Melter', 'Sticky Fuel', 'Scorching Tide'],
        ['Improved Thermal Efficiency', 'Tuned Cooler', 'Flow Rate Expansion', 'Ice Spear', 'Crystal Nucleation', 'Ice Storm', 'Snowball'],
        ['Hydrogen Ion Additive', 'AG Mixture', 'Volatile Impact Mixture', 'Disperser Compound', 'Combustive Goo Mix', 'Goo Bomber Special', 'Sludge Blast']
    ],[
        ['Stunner', 'Light-Weight Magazines', 'Magnetic Pellet Alignment', 'Cycle Overload', 'Mini Shells', 'Pump Action'],
        ['Super-Slim Rounds', 'Well Oiled Machine', 'EM Refire Booster', 'Light-Weight Rounds', 'Hyperalloy Assembly', 'Micro-Conductor Add-On', 'Turret EM Discharge'],
        ['Eraser', 'Armor Break Module', 'Explosive Chemical Rounds', 'Seeker Rounds', 'Executioner', 'Neuro-Lasso', 'SMЯT Trigger OS™']
    ], [
       ['A Little More Oomph!', 'Thinned Drum Walls', 'Burning Hell', 'Compact Feed Mechanism', 'Exhaust Vectoring', 'Rotary Overdrive', 'Bullet Hell', 'Lead Storm'],
       ['Composite Drums', 'Splintering Shells', 'Carpet Bomber', 'Combat Mobility', 'Big Bertha', 'Neurotoxin Payload', 'Mortar Rounds'],
       ['Overtuned Feed Mechanism', 'Fragmentation Missiles', 'Plasma Burster Missiles', 'Minelayer System', 'Rocket Barrage', 'Jet Fuel Homebrew', 'Salvo Module', 'Cluster Charges'] 
    ], [
        ['Compact Ammo', 'Gas Rerouting', 'Homebrew Powder', 'Overclocked Firing Mechanism', 'Bullets of Mercy', 'Burst Fire', 'AI Stability Engine', 'Electrifying Reload'],
        ['Hoverclock', 'Minimal Clips', 'Active Stability System', 'Hipster', 'Electrocuting Focus Shots', 'Supercooling Chamber', 'Marked for Death'],
        ['Aggressive Venting', 'Thermal Liquid Coolant', 'Impact Deflection', 'Conductive Thermals', 'Rewiring Mod', 'Overtuned Particle Accelerator', 'Shield Battery Booster', 'Thermal Exhaust Feedback']
    ]]
secondaryOC = [[
        ['Chain Hit', 'Homebrew Powder', 'Oversized Magazine', 'Automatic Fire', 'Explosive Reload', 'Tranquilizer Rounds'],
        ['Energy Rerouting', 'Magnetic Cooling Unit', 'Heat Pipe', 'Heavy Hitter', 'Overcharger', 'Persistent Plasma'],
        ['Liquid Cooling System', 'Super Focus Lens', 'Diffusion Ray', 'Mega Power Supply', 'Blistering Necrosis', 'Gamma Contamination']
    ],[
        ['Clean Sweep', 'Pack Rat', 'Compact Rounds', 'RJ250 Compound', 'Fat Boy', 'Hyper Propellant'],
        ['Light-Weight Cases', 'Roll Control', 'Stronger Plasma Current', 'Return to Sender', 'High Voltage Crossover', 'Spinning Death', 'Inferno'],
        ['Efficiency Tweaks', 'Automated Beam Controller', 'Feedback Loop', 'Volatile Impact Reactor', 'Plastcrete Catalyst', 'Overdrive Booster']
    ],[
        ['Chain Hit', 'Homebrew Powder', 'Volatile Bullets', 'Six Shooter', 'Elephant Rounds', 'Magic Bullets'],
        ['Composite Casings', 'Full Chamber Seal', 'Compact Mags', 'Experimental Rounds', 'Electro Minelets', 'Micro Flechettes', 'Lead Spray'],
        ['Re-Atomizer', 'Ultra-Magnetic Coils', 'Backfeeding Module', 'The Mole', 'Hellfire', 'Triple-Tech Chambers']
    ], [
        ['Compact Shells', 'Special Powder', 'Stuffed Shells', 'Shaped Shells', 'Jumbo Shells', 'Double Barrel'],
        ['Minimal Magazines', 'Custom Casings', 'Cryo Minelets', 'Embedded Detonators', 'Gas Recycling'],
        ['Quick Fire', 'The Specialist', 'Cryo Bolt', 'Fire Bolt', 'Bodkin Points', 'Trifork Volley']
    ]]

# Converts raw json into a cleaner format

# opts is the number of mods for the build
def modStruct(opts):
    return [[0, 0, 0] for _ in range(opts)]

def arrayMods(num, opts):
    return [modStruct(opts) for _ in range(num)]

def ocStruct(isPrimary, slot, cls):
    allOCs = primaryOC if isPrimary else secondaryOC
    ocs = allOCs[cls][slot]

    ocDict = {oc: 0 for oc in ocs}
    ocDict['None'] = 0
    return ocDict

def weaponStruct(isPrimary, cls):
    return [
        {
            'count': 0,
            'mods': modStruct(5),
            'oc': ocStruct(isPrimary, i, cls),
        } for i in range(3)
    ]

# ['Driller', 'Engineer', 'Gunner', 'Scout']

builds = [
    # Driller
    {
        'primary': weaponStruct(True, 0),
        'secondary': weaponStruct(False, 0),
        'mobility': modStruct(4),
        'utility': modStruct(4),
        'armor': modStruct(4),
        'pickaxe': modStruct(2),
        'grenade': [0, 0, 0, 0],
    },
    # Engineer
    {
        'primary': weaponStruct(True, 1),
        'secondary': weaponStruct(False, 1),
        'mobility': modStruct(3),
        'utility': modStruct(4),
        'armor': modStruct(4),
        'pickaxe': modStruct(2),
        'grenade': [0, 0, 0, 0],
    },
    # Gunner
    {
        'primary': weaponStruct(True, 2),
        'secondary': weaponStruct(False, 2),
        'mobility': modStruct(3),
        'utility': modStruct(3),
        'armor': modStruct(4),
        'pickaxe': modStruct(2),
        'grenade': [0, 0, 0, 0],
    },
    # Scout
    {
        'primary': weaponStruct(True, 3),
        'secondary': weaponStruct(False, 3),
        'mobility': modStruct(4),
        'utility': modStruct(3),
        'armor': modStruct(4),
        'pickaxe': modStruct(2),
        'grenade': [0, 0, 0, 0],
    },
]

print(builds)

jsonNumKeys = {
    '1': 0,
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4
}

def addWeapon(build, key):
    global builds

    rawWeapon = build[key]
    weaponIndex = rawWeapon['index']

    dataWeapon = builds[build['class']][key][weaponIndex]

    # increment count
    dataWeapon['count'] += 1

    # increment mod counts
    for rawKey, dataKey in jsonNumKeys.items():
        if rawKey in rawWeapon:
            dataWeapon['mods'][dataKey][rawWeapon[rawKey] - 1] += 1

    # set oc
    oc = build[key]['oc'] if 'oc' in build[key] else 'None'
    dataWeapon['oc'][oc] += 1

def addEquipment(build, key):
    rawEquipment = build[key]
    dataEquipment = builds[build['class']][key]

    for rawKey, dataKey in jsonNumKeys.items():
        if rawKey in rawEquipment:
            # Increment the count
            dataEquipment[dataKey][rawEquipment[rawKey] - 1] += 1

def addGrenade(build):
    rawGrenade = build['grenade']
    builds[build['class']]['grenade'][rawGrenade - 1] += 1

with open('raw.json') as f:
    rawBuilds = json.load(f)

    for build in rawBuilds:
        if build['primary']:
            addWeapon(build, 'primary')
        if build['secondary']:
            addWeapon(build, 'secondary')
        if build['mobility']:
            addEquipment(build, 'mobility')
        if build['utility']:
            addEquipment(build, 'utility')
        if build['armor']:
            addEquipment(build, 'armor')
        if build['pickaxe']:
            addEquipment(build, 'pickaxe')
        if build['grenade']:
            addGrenade(build)

with open('parsed.json', 'w') as f:
    # compact
    # f.write(json.dumps(builds, separators=(',',':')))
    f.write(json.dumps(builds, indent=2))
