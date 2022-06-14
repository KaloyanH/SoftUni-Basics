import math

count_mags = int(input())
count_zum = int(input())
count_roses = int(input())
count_cactus = int(input())
present_price = float(input())

price_mags = 3.25
price_zum = 4
price_roses = 3.5
price_cactus = 8

overall_sum = count_mags * price_mags + count_zum * price_zum + \
    count_roses * price_roses + count_cactus * price_cactus

after_taxes = overall_sum - overall_sum*0.05

if after_taxes >= present_price:
    money_left = after_taxes - present_price
    print(f'She is left with {math.floor(money_left)} leva.')

else:
    money_needed = present_price - after_taxes
    print(f'She will have to borrow {math.ceil(money_needed)} leva.')
