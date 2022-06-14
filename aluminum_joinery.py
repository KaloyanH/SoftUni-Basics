count_joinery = int(input())
type_joinery = input()
delivery = input()

price_90X130 = 110
price_100X150 = 140
price_130X180 = 190
price_200X300 = 250
price_delivery = 60

if 10 <= count_joinery < 30 and type_joinery == '90X130' and delivery == 'With delivery':
    price_joinery = price_90X130 * count_joinery + price_delivery
    print(f'{price_joinery} BGN')

elif 10 <= count_joinery < 30 and type_joinery == '90X130' and delivery == 'Without delivery':
    price_joinery = price_90X130 * count_joinery
    print(f'{price_joinery} BGN')



