budget = float(input())
season = input()

accommodation = ""
location = ""
vacation_price = 0

if budget <= 1000:
    accommodation = "Camp"
    if season == "Summer":
        location = "Alaska"
        vacation_price = budget * 0.65
    elif season == "Winter":
        location = "Morocco"
        vacation_price = budget * 0.45
elif 1000 < budget <= 3000:
    accommodation = "Hut"
    if season == "Summer":
        location = "Alaska"
        vacation_price = budget * 0.8
    elif season  == "Winter":
        location = "Morocco"
        vacation_price = budget * 0.6
elif budget > 3000:
    accommodation = "Hotel"
    vacation_price = budget * 0.9
    if season == "Summer":
        location = "Alaska"
    else:
        location = "Morocco"

print(f"{location} - {accommodation} - {vacation_price:.2f}")


