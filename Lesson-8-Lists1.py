cities = ['Moscow','Washington','Beijing','Paris','Berlin']
print(cities)
print(len(cities))

print("#update")

print("city №3 is\t", cities[2])
print("last city is\t", cities[-1])
cities[2] = 'Tokyo'
print(cities)

print("#add")

cities.append('Madrid')
cities.insert(1, 'Saint-Petersburg')
print(cities)
print(len(cities))

print("#delete")

del cities[-1]
print(cities)

cities.remove('Washington')
print(cities)

deleted_city = cities.pop()
print("deleted city is\t", deleted_city)

print("#reverse")

cities.reverse()
print(cities)

print("#sort")

cities.sort()
print(cities)

cities.sort(reverse=True)
print(cities)

print("#output")

for item in cities:
    print(item)