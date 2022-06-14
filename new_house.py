type_of_flowers = input()
count_flowers = int(input())
budget = int(input())

price_roses = 5
price_dahlias = 3.80
price_tulips = 2.80
price_narcissus = 3
price_gladiolas = 2.50

overall_price = 0

if type_of_flowers == "Roses":
    if count_flowers > 80:
        overall_price = price_roses*count_flowers*0.9
    else:
        overall_price = price_roses*count_flowers
elif type_of_flowers == "Dahlias":
    if count_flowers > 90:
        overall_price = price_dahlias*count_flowers*0.85
    else:
        overall_price = price_dahlias * count_flowers
elif type_of_flowers == "Tulips":
    if count_flowers > 80:
        overall_price = price_tulips * count_flowers * 0.85
    else:
        overall_price = price_tulips * count_flowers
elif type_of_flowers == "Narcissus":
    if count_flowers < 120:
        overall_price = price_narcissus * count_flowers * 1.15
    else:
        overall_price = price_narcissus * count_flowers
elif type_of_flowers == "Gladiolus":
    if count_flowers < 80:
        overall_price = price_gladiolas * count_flowers * 1.2
    else:
        overall_price = price_gladiolas * count_flowers

difference = abs(budget - overall_price)

if budget >= overall_price:
    print(f'Hey, you have a great garden with {count_flowers} {type_of_flowers} and {difference:.2f} leva left.')
elif budget < overall_price:
    print(f'Not enough money, you need {difference:.2f} leva more.')
