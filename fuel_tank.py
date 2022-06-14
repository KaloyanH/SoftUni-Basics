name = input()
liters = float(input())

if liters >= 25 and name == 'Diesel':
    print('You have enough diesel.')

elif liters < 25 and name == 'Diesel':
    print('Fill your tank with diesel!')

elif liters >= 25 and name == 'Gasoline':
    print('You have enough gasoline.')

elif liters < 25 and name == 'Gasoline':
    print('Fill your tank with gasoline!')

elif liters >= 25 and name == 'Gas':
    print('You have enough gas.')

elif liters < 25 and name == 'Gas':
    print('Fill your tank with gas!')

else:
    print('Invalid fuel!')

