number_juniors = int(input())
number_seniors = int(input())
type_of_race = input()

total_tax_juniors = 0
total_tax_seniors = 0

if type_of_race == "trail":
    total_tax_juniors = number_juniors * 5.50
    total_tax_seniors = number_seniors * 7
elif type_of_race == "cross-country":
    total_tax_juniors = number_juniors * 8
    total_tax_seniors = number_seniors * 9.50
elif type_of_race == "downhill":
    total_tax_juniors = number_juniors * 12.25
    total_tax_seniors = number_seniors * 13.75
elif type_of_race == "road":
    total_tax_juniors = number_juniors * 20
    total_tax_seniors = number_seniors * 21.50

sum_taxes = total_tax_juniors + total_tax_seniors

if type_of_race == "cross-country" and number_juniors + number_seniors >= 50:
    sum_taxes -= sum_taxes * 0.25

expenses = sum_taxes * 0.05
donated_sum = sum_taxes - expenses
print(f"{donated_sum:.2f}")
