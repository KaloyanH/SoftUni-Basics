month = input()
days_of_stay = int(input())

studio_price = 0
apt_price = 0


if month == "May" or month == "October":
    studio_price = 50
    apt_price = 65
    if 7 < days_of_stay < 14:
        studio_price = 50 - (50*0.05)
        apt_price = 65
    elif days_of_stay > 14:
        studio_price = 50 - (50*0.3)
        apt_price = 65 - (65*0.1)

if month == "June" or month == "September":
    studio_price = 75.20
    apt_price = 68.70
    if days_of_stay > 14:
        studio_price = 75.20 - (75.20*0.2)
        apt_price = 68.70 - (68.70*0.1)

if month == "July" or month == "August":
    studio_price = 76
    apt_price = 77
    if days_of_stay > 14:
        apt_price = 77 - (77*0.1)

sum_apt_price = days_of_stay * apt_price
sum_studio_price = days_of_stay * studio_price

print(f"Apartment: {sum_apt_price:.2f} lv.")
print(f"Studio: {sum_studio_price:.2f} lv.")







