age = int(input())
washing_machine_price = float(input())
price_of_toys = int(input())

saved_money = 0
number_of_toys = 0
birthday_money = 0

for birthdays in range(1, age + 1):
    if birthdays % 2 == 0:
        birthday_money += 10
        saved_money += birthday_money - 1
    else:
        number_of_toys += 1

total_money = saved_money + (price_of_toys * number_of_toys)
difference = abs(total_money - washing_machine_price)

if total_money >= washing_machine_price:
    print(f'Yes! {difference:.2f}')
else:
    print(f"No! {difference:.2f}")

