days_of_stay = int(input())
type_of_premise = input()
evaluation = input()

nights_of_stay = days_of_stay - 1
room_for_1_person = 18
apartment = 25
president_apartment = 35
total_price = 0

if type_of_premise == "room for one person":
    total_price = nights_of_stay * room_for_1_person
elif type_of_premise == "apartment":
    if days_of_stay < 10:
        total_price = nights_of_stay * apartment - (nights_of_stay * apartment) * 0.3
    elif 10 <= days_of_stay <= 15:
        total_price = nights_of_stay * apartment - (nights_of_stay * apartment) * 0.35
    elif days_of_stay > 15:
        total_price = nights_of_stay * apartment - (nights_of_stay * apartment) * 0.5
elif type_of_premise == "president apartment":
    if days_of_stay < 10:
        total_price = nights_of_stay * president_apartment - (nights_of_stay * president_apartment) * 0.1
    elif 10 <= days_of_stay <= 15:
        total_price = nights_of_stay * president_apartment - (nights_of_stay * president_apartment) * 0.15
    elif days_of_stay > 15:
        total_price = nights_of_stay * president_apartment - (nights_of_stay * president_apartment) * 0.2

if evaluation == "positive":
    total_price = total_price + total_price * 0.25
elif evaluation == "negative":
    total_price = total_price - total_price * 0.1

print(f"{total_price:.2f}")





