fruit_name = input()
day_of_the_week = input()
quantity = float(input())

total_sum = 0
price = 0
invalid = False

if day_of_the_week == 'Monday' or day_of_the_week == 'Tuesday' or day_of_the_week == 'Wednesday' or day_of_the_week == 'Thursday' or day_of_the_week == 'Friday':
        if fruit_name == 'banana':
            price = 2.50
        elif fruit_name == 'apple':
            price = 1.2
        elif fruit_name == 'orange':
            price = 0.85
        elif fruit_name == 'grapefruit':
            price = 1.45
        elif fruit_name == 'kiwi':
            price = 2.70
        elif fruit_name == "pineapple":
            price = 5.50
        elif fruit_name == "grapes":
            price = 3.85
        else:
            invalid = True
elif day_of_the_week == 'Saturday' or day_of_the_week == "Sunday":
        if fruit_name == 'banana':
            price = 2.70
        elif fruit_name == 'apple':
            price = 1.25
        elif fruit_name == 'orange':
            price = 0.9
        elif fruit_name == 'grapefruit':
            price = 1.6
        elif fruit_name == 'kiwi':
            price = 3
        elif fruit_name == "pineapple":
            price = 5.60
        elif fruit_name == "grapes":
            price = 4.20
        else:
            invalid = True
else:
    invalid = True

if invalid is True:
    print('error')

else:
    total_sum = quantity * price
    print(f'{total_sum:.2f}')
