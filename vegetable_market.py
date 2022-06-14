price_vegetables = float(input())
price_fruits = float(input())
kg_vegetables = int(input())
kg_fruits = int(input())
eur_rate = 1.94

overall_income = price_vegetables*kg_vegetables + price_fruits*kg_fruits

overall_income_in_euro = overall_income / eur_rate

print(f'{overall_income_in_euro :.2f}')

