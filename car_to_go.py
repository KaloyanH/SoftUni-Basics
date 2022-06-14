budget = float(input())
season = input()

car_price = 0
car_class = ""
type_car = ""

if budget <= 100:
    car_class = "Economy class"
    if season == "Summer":
        type_car = "Cabrio"
        car_price = budget*0.35
    elif season == "Winter":
        type_car = "Jeep"
        car_price = budget*0.65

elif 100 < budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        type_car = "Cabrio"
        car_price = budget*0.45
    elif season == "Winter":
        type_car = "Jeep"
        car_price = budget*0.8

elif budget > 500:
    car_class = "Luxury class"
    type_car = "Jeep"
    car_price = budget*0.9

print(car_class)
print(f"{type_car} - {car_price:.2f}")
