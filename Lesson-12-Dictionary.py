#           (-------Item------)
#           (key)       (value)
enemy = {
            'loc_x':    70,
            'loc_y':    50,
            "color":    'green',
            'health':   100,
            'name':     'Mudillo'
}

all_enemies = []

for x in range(0,3):
    #print(x)
    all_enemies.append(enemy.copy())
    #all_enemies[x]['loc_x'] = all_enemies[x]['loc_x'] + 10 # не сработало

all_enemies[1]['health'] = 30

for ene in all_enemies:
    print(ene)