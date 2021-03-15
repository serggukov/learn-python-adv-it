for x in range(0, 3):
    print("*****")
    print("----------")

print()

for x in range(0, 10, 2): # вывести x с шагом 2
    print(x)

print()

for x in range(5, 0, -1): # вывести x в обратном порядке
    print(x)

print()

x = 1
while True:
    print(x)
    x = x + 1
    if x > 10:
        break