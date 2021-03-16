age = 31

if age <= 4:
    print("You are baby!")
elif age > 4 and age < 12:
    print("You are kid!")
elif age > 12 and age < 19:
    print("You are teenager!")
else:
    print("You are old!")

print("----END----")

all_cars = ["audi", "toyota", "kia", "bmw", "ferrari", "nissan", "mercedes", "lamborghini"]
german_cars = ["audi", "bmw", "mercedes"]

for car in all_cars:
    if car in german_cars:
        print(car + " is german car")
    #else:
    #    print(car + " is Not german car")

print("----END----")