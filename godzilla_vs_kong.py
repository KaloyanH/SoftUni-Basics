budget = float(input())
extras = int(input())
price_clothing = float(input())

decors = budget*0.1

if extras >=150:
    price_clothing -= price_clothing*0.1

overall_clothing = extras*price_clothing
sum_budget = decors + overall_clothing

budget_difference = abs(budget - sum_budget)

if budget < sum_budget:
    print('Not enough money!')
    print(f'Wingard needs {budget_difference:.2f} leva more.')

else:
    print('Action!')
    print(f'Wingard starts filming with {budget_difference:.2f} leva left.')