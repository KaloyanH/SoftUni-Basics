inherited_money = float(input())
year_to_survive = int(input())


years = 18

for year_to_survive in range(1800, year_to_survive+1):
    if year_to_survive % 2 == 0:
        inherited_money -= 12000
    else:
        inherited_money -= 12000 + 50*years

    years += 1

if inherited_money >= 0:
    print(f"Yes! He will live a carefree life and will have {inherited_money:.2f} dollars left.")
else:
    print(f"He will need {abs(inherited_money):.2f} dollars to survive.")
