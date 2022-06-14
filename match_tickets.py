budget = float(input())
category = input()
number_of_people = int(input())

transport_money = 0
vip_ticket = 499.99
normal_ticket = 249.99
sum_tickets = 0

if category == "VIP":
    sum_tickets = vip_ticket * number_of_people
elif category == "Normal":
    sum_tickets = normal_ticket * number_of_people

if number_of_people <= 4:
    transport_money = budget * 0.75
elif number_of_people <= 9:
    transport_money = budget * 0.6
elif number_of_people <= 24:
    transport_money = budget * 0.5
elif number_of_people <= 49:
    transport_money = budget * 0.4
elif number_of_people >= 50:
    transport_money = budget * 0.25

total_expenses = sum_tickets + transport_money
money_difference = abs(budget - total_expenses)

if budget >= total_expenses:
    print(f"Yes! You have {money_difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {money_difference:.2f} leva.")


