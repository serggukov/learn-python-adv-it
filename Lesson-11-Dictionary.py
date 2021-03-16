#           (-------Item------)
#           (key)       (value)
enemy = {
            'loc_x':    70,
            'loc_y':    50,
            "color":    'green',
            'health':   100,
            'name':     'Mudillo'
}

print(enemy)
print("Location x is", enemy['loc_x'])

# add
enemy['rank'] = 'Admiral'
print(enemy)

# del
del enemy['rank']
print(enemy)

enemy['loc_x'] = enemy['loc_x'] + 40
enemy['health'] = enemy['health'] - 30
if enemy['health'] < 80:
    enemy['color'] = 'yellow'
print(enemy)

print(enemy.keys())
print(enemy.values())