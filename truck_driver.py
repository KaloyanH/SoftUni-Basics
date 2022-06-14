season = input()
mileage_per_month = float(input())

payment_per_month = 0

if mileage_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        payment_per_month = mileage_per_month * 0.75
    elif season == "Summer":
        payment_per_month = mileage_per_month * 0.9
    elif season == "Winter":
        payment_per_month = mileage_per_month * 1.05

elif 5000 < mileage_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        payment_per_month = mileage_per_month * 0.95
    elif season  == "Summer":
        payment_per_month = mileage_per_month * 1.1
    elif season == "Winter":
        payment_per_month = mileage_per_month * 1.25

elif mileage_per_month > 10000:
    payment_per_month = mileage_per_month * 1.45

total_salary = payment_per_month * 4
taxes = total_salary * 0.1
total_profit = total_salary - taxes

print(f"{total_profit:.2f}")