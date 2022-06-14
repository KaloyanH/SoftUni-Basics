price_of_vacation = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_teddies = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

price_of_puzzle = 2.6
price_of_dolls = 3
price_of_teddies = 4.1
price_of_minion = 8.2
price_of_truck = 2

total_toys = number_of_puzzles + number_of_dolls + number_of_teddies + \
              number_of_minions + number_of_trucks

total_price = number_of_puzzles * price_of_puzzle + \
              number_of_dolls * price_of_dolls + \
              number_of_teddies * price_of_teddies + \
              number_of_minions * price_of_minion + \
              number_of_trucks * price_of_truck

if total_toys >= 50:
    total_price -= total_price*0.25

overall_sum = total_price - total_price * 0.1
money_balance = abs(overall_sum - price_of_vacation)

if overall_sum >= price_of_vacation:
    print(f'Yes! {money_balance:.2f} lv left.')

else:
    print(f'Not enough money! {money_balance:.2f} lv needed.')


