mynumber_list = list(range(0, 10))
print(mynumber_list)

r = mynumber_list.sort(reverse=True)
print(mynumber_list)
print("Max is: " + str(max(mynumber_list)))
print("Min is: " + str(min(mynumber_list)))
print("Sum is: " + str(sum(mynumber_list)))

for x in mynumber_list:
    x = x * 2
    #print(x)

#         0        1        2     3      4
cars = ['bmw','mercedes','audi','vw','porsche']
'''
for car in cars:
    print(car.upper())
'''
print(cars[1:4])
print(cars[:4])
print(cars[-3:-1])

cars_copy = cars[:] # copy of list