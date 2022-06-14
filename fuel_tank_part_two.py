fuel = input()
liters = float(input())
discount_card = input()

gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93


discount_gasoline_per_liter = gasoline_price - 0.18
discount_diesel_per_liter = diesel_price - 0.12
discount_gas_per_liter = gas_price - 0.08

if 20 <= liters < 26 and fuel == "Gasoline" and discount_card == "Yes":
    sum_gasoline = liters * discount_gasoline_per_liter
    total_sum = sum_gasoline - sum_gasoline*0.08
    print(f'{total_sum:.2f} lv.')

elif 20 <= liters < 26 and fuel == "Gasoline" and discount_card == "No":
    sum_gasoline = liters * gasoline_price
    total_sum = sum_gasoline - sum_gasoline * 0.08
    print(f'{total_sum:.2f} lv.')

elif liters > 25 and fuel == "Gasoline" and discount_card == "Yes":
    sum_gasoline = liters * discount_gasoline_per_liter
    total_sum = sum_gasoline - sum_gasoline*0.10
    print(f'{total_sum:.2f} lv.')

elif liters > 25 and fuel == "Gasoline" and discount_card == "No":
    sum_gasoline = liters * gasoline_price
    total_sum = sum_gasoline - sum_gasoline * 0.10
    print(f'{total_sum:.2f} lv.')

if 20 <= liters < 26 and fuel == "Diesel" and discount_card == "Yes":
    sum_diesel = liters * discount_diesel_per_liter
    total_sum = sum_diesel - sum_diesel*0.08
    print(f'{total_sum:.2f} lv.')

elif 20 <= liters < 26 and fuel == "Diesel" and discount_card == "No":
    sum_diesel = liters * diesel_price
    total_sum = sum_diesel - sum_diesel * 0.08
    print(f'{total_sum:.2f} lv.')

elif liters > 25 and fuel == "Diesel" and discount_card == "Yes":
    sum_diesel = liters * discount_diesel_per_liter
    total_sum = sum_diesel - sum_diesel*0.10
    print(f'{total_sum:.2f} lv.')

elif liters > 25 and fuel == "Diesel" and discount_card == "No":
    sum_diesel = liters * diesel_price
    total_sum = sum_diesel - sum_diesel * 0.10
    print(f'{total_sum:.2f} lv.')

if 20 <= liters < 26 and fuel == "Gas" and discount_card == "Yes":
    sum_gas = liters * discount_gas_per_liter
    total_sum = sum_gas - sum_gas*0.08
    print(f'{total_sum:.2f} lv.')

elif 20 <= liters < 26 and fuel == "Gas" and discount_card == "No":
    sum_gas = liters * gas_price
    total_sum = sum_gas - sum_gas * 0.08
    print(f'{total_sum:.2f} lv.')

elif liters > 25 and fuel == "Gas" and discount_card == "Yes":
    sum_gas = liters * discount_gas_per_liter
    total_sum = sum_gas - sum_gas*0.10
    print(f'{total_sum:.2f} lv.')

elif liters > 25 and fuel == "Gas" and discount_card == "No":
    sum_gas = liters * gas_price
    total_sum = sum_gas - sum_gas * 0.10
    print(f'{total_sum:.2f} lv.')

elif liters < 20 and fuel == "Gas" and discount_card == "Yes":
     total_sum = liters * discount_gas_per_liter
     print(f'{total_sum:.2f} lv.')

elif liters < 20 and fuel == "Gas" and discount_card == "No":
     total_sum = liters * gas_price
     print(f'{total_sum:.2f} lv.')

elif liters < 20 and fuel == "Gasoline" and discount_card == "Yes":
    total_sum = liters * discount_gasoline_per_liter
    print(f'{total_sum:.2f} lv.')

elif liters < 20 and fuel == "Gasoline" and discount_card == "No":
    total_sum = liters * gasoline_price
    print(f'{total_sum:.2f} lv.')

elif liters < 20 and fuel == "Diesel" and discount_card == "Yes":
    total_sum = liters * discount_diesel_per_liter
    print(f'{total_sum:.2f} lv.')

elif liters < 20 and fuel == "Diesel" and discount_card == "No":
    total_sum = liters * diesel_price
    print(f'{total_sum:.2f} lv.')
