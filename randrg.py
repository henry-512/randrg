import PySimpleGUI as sg
import random as rng
import json
# rng.randint(0, 10) inc 0,10

# DRG Build Randomizer
# Updated for Season 5

classes = ['Driller', 'Engineer', 'Gunner', 'Scout']
primary = [['Flame', 'Cryo', 'Sludge'],
    ['Warthog', 'Stubby', 'LOKI'],
    ['Minigun', 'Auto', 'Hurricane'],
    ['GK2', 'M1000', 'DRAK']]
primaryUpgrades = [[23332, 33232, 33222],
    [23322, 33233, 23323],
    [32333, 33323, 32223],
    [32223, 23223, 32332]]
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
secondary = [['Subata', 'EPC', 'Cooker'],
    ['PGL', 'Breach', 'Shard'],
    ['Bulldog', 'BRT', 'Coilgun'],
    ['Boomstick', 'Zhukov', 'Boltshark']]
secondaryUpgrades = [[22333, 32333, 33223],
    [32333, 23223, 32223],
    [23322, 33232, 33223],
    [22333, 23232, 33223]]
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

grenade = [['Impact Axe', 'High Explosive', 'Neurotoxin', 'Springloaded'],
    ['LURE', 'Plasma Burster', 'Proximity Mine', 'Shredder'],
    ['Sticky', 'Incendiary', 'Cluster', 'Leadburster'],
    ['Inhibitor-Field', 'Cryo', 'Pheromone',  'Voltaic']
]

mobilityNames = ['Drills', 'Platform', 'Zipline', 'Grapple']
utilityNames = ['C4', 'Turret', 'Shield', 'Flare']

mobilityUpgrades = [3212, 313, 312, 2123]
utilityUpgrades = [3123, 2332, 223, 223]
armor = 3213
pick = 13

active = ['Beast Master', 'Berzerker', 'Dash', 'Field Medic', 'Heightened Senses', 'Hover Boots', 'Iron Will', 'See You In Hell', 'Shield Link']
passive = ['Born Ready', 'Deep Pockets', 'Elemental Insulation', 'Friendly', 'It\'s a Bug Thing', 'Resupplier', 'Second Wind', 'Strong Arm', 'Sweet Tooth', 'Thorns', 'Unstoppable', 'Vampire', 'Veteran Depositor']

sg.theme('DarkAmber')   # Add a touch of color
sg.set_options(element_padding=(0,0))  

# All the stuff inside your window.
layout = [
    [sg.Text('DRG Randomizer', size=(54,1))],
    [sg.Button('Randomize', key='unlucky'), sg.Button("I'm feeling lucky", key='lucky'), sg.Button('Netdeck', key='netdeck')],
    [sg.Text('Class'), sg.Text(key='class')],
    [sg.Text('Primary'), sg.Text(key='pr'), sg.Text(key='prBld', size=(7,1)), sg.Text(key='prOc', size=(25,1))],
    [sg.Text('Secondary'), sg.Text(key='sc'), sg.Text(key='scBld', size=(7,1)), sg.Text(key='scOc', size=(25,1))],
    [sg.Text('Mobility Tool'), sg.Text(key='mbName'), sg.Text(key='mb')],
    [sg.Text('Utility Tool'), sg.Text(key='utName'), sg.Text(key='ut')],
    [sg.Text('Armor'), sg.Text(key='ar')],
    [sg.Text('Grenade'), sg.Text(key='gn', size=(44,1))],
    [sg.Text('Pickaxe'), sg.Text(key='pk')],
    [sg.Text('Actives'), sg.Text(key='pa', size=(44,1))],
    [sg.Text('Passives'), sg.Text(key='pp', size=(44,1))],
    [sg.Text(''.join('-' for _ in range(108)), size=(54,1))],
    [sg.Text('Meta'), sg.Text(key='meta'), sg.Text('Netdecked'), sg.Text('Viability'), sg.Text(key='viability')]
]

# Create the Window
window = sg.Window('DRG Build Randomizer', layout, default_element_size=(10,1), auto_size_text=False, auto_size_buttons=False, default_button_element_size=(18,1), finalize=True)

# Ok this one's pretty bad
# Randomizes the upgrade numbers from the maximum for each option
def getNum(max: int):
    return ''.join(str(rng.randint(1, int(s))) for s in str(max))

def calcMod(maxMod: int, b={}):
    modAr = [rng.randint(0, int(s) - 1) for s in str(maxMod)]
    b['mods'] = modAr
    b['mod'] = ''.join(str(m + 1) for m in modAr)
    return b

def randomWeapon(cls, isPrimary):
    weaponIndex = rng.randint(0,2)
    
    names = primary if isPrimary else secondary
    oc = primaryOC if isPrimary else secondaryOC
    mod = primaryUpgrades if isPrimary else secondaryUpgrades

    return calcMod(mod[cls][weaponIndex], {
        'index': weaponIndex,
        'oc': rng.choice(oc[cls][weaponIndex]),
        'name': names[cls][weaponIndex]
    })

def randomEquipment(cls, isMobility):
    names = mobilityNames if isMobility else utilityNames
    maxes = mobilityUpgrades if isMobility else utilityUpgrades
    return calcMod(maxes[cls], { 'name': names[cls], }), len(str(maxes[cls]))

def metaWeapon(cls, key, weapon):
    totalMeta = 1

    print('--------------')

    with open('meta.json') as f:
        meta = json.load(f)[cls][key]

        # calc mod meta
        for i, mod in enumerate(meta['mod'][weapon['index']]):
            # totalMeta += mod[weapon['mods'][i]]
            print(mod[weapon['mods'][i]])
            totalMeta *= mod[weapon['mods'][i]]

        # calc oc meta
        # totalMeta += 2 * meta['oc'][weapon['index']][weapon['oc']]
        print(meta['oc'][weapon['index']][weapon['oc']])
        totalMeta *= meta['oc'][weapon['index']][weapon['oc']]

    print(totalMeta)

    return totalMeta

def metaEquipment(cls, key, equip):
    totalMeta = 0

    with open('meta.json') as f:
        meta = json.load(f)[cls][key]

        for i, mod in enumerate(meta):
            totalMeta += mod[equip['mods'][i]]
    return totalMeta


# def mostMeta(cls, primary, secondary)


# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break
    if event == 'lucky' or event == 'unlucky' or event == 'netdeck':
        rClass = rng.randint(0,3)

        # The luck factor (25% more engineer)
        if event == 'lucky' and rng.randint(0,3) == 0:
            rClass = 1

        # if event == 'netdeck':
        #     rPrimary = {'mods': [1, 1, 1, 2, 0], 'mod': 22231, 'index': 0, 'oc': 'Sticky Fuel', 'name': 'Flame'}
        # else:

        totalMetaCount = 14

        rPrimary = randomWeapon(rClass, True)
        rSecondary = randomWeapon(rClass, False)
        rMobility, x = randomEquipment(rClass, True)
        totalMetaCount += x
        rUtility, x = randomEquipment(rClass, False)
        totalMetaCount += x
        rArmor = calcMod(armor)

        # print('meta')
        # totalMeta = \
        #     + metaWeapon(rClass, 'primary', rPrimary)\
        #     + metaWeapon(rClass, 'secondary', rSecondary)\
        #     + metaEquipment(rClass, 'mobility', rMobility)\
        #     + metaEquipment(rClass, 'utility', rUtility)\
        #     + metaEquipment(rClass, 'armor', rArmor)
        # print('000')
        # print(totalMeta)
        # print(totalMetaCount)
        # print(totalMeta / totalMetaCount)

        # Update screen
        window['class'].Update(classes[rClass])

        # primary
        window['pr'].Update(rPrimary['name'])
        window['prBld'].Update(rPrimary['mod'])
        window['prOc'].Update(rPrimary['oc'])

        # secondary
        window['sc'].Update(rSecondary['name'])
        window['scBld'].Update(rSecondary['mod'])
        window['scOc'].Update(rSecondary['oc'])

        window['mbName'].Update(rMobility['name'])
        window['mb'].Update(rMobility['mod'])
        window['utName'].Update(rUtility['name'])
        window['ut'].Update(rUtility['mod'])
        window['ar'].Update(rArmor['mod'])

        # These aren't tracked by karl so we generate them manually
        window['pk'].Update(getNum(pick))
        window['gn'].Update(grenade[rClass][rng.randint(0,2)])

        # Gets 2 random numbers from 0-X then converts to perk name, then makes them a pretty string
        window['pa'].Update(', '.join(active[p] for p in rng.sample(range(0,len(active)-1), 2)))
        window['pp'].Update(', '.join(passive[p] for p in rng.sample(range(0,len(passive)-1), 3)))

        window['pp'].Update(', '.join(passive[i] for i in (2,12,4)))

window.close()