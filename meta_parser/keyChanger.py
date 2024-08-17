import json

# Intermediate fixer

grenades = [
    0,
    1, 2, 3,
    1, 2, 3,
    1, 2, 3,
    1, 2, 3,
    # new grenades
    4, 4, 4, 4
]

aaaa = set()
with open('raw.txt') as f:
    data = json.loads('[' + f.read()[:-2] + ']')

    for d in data:
        if d['grenade'] == None:
            d['grenade'] = 0
        
        d['grenade'] = grenades[d['grenade']]
    
    with open('raw.json', 'w') as of:
        of.write(json.dumps(data))
