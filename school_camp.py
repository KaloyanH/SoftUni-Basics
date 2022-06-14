season = input()
type_of_group = input()
number_of_students = int(input())
number_of_stays = int(input())

activity = ""
accommodation_price = 0

if season == "Winter":
    if type_of_group == "boys" or type_of_group == "girls":
        accommodation_price = number_of_stays * number_of_students * 9.60
        if type_of_group == "boys":
            activity = "Judo"
        elif type_of_group == "girls":
            activity = "Gymnastics"
    if type_of_group == "mixed":
        accommodation_price = number_of_stays * number_of_students * 10
        activity = "Ski"
elif season == "Spring":
    if type_of_group == "boys" or type_of_group == "girls":
        accommodation_price = number_of_stays * number_of_students * 7.20
        if type_of_group == "boys":
            activity = "Tennis"
        elif type_of_group == "girls":
            activity = "Athletics"
    if type_of_group == "mixed":
        accommodation_price = number_of_stays * number_of_students * 9.50
        activity = "Cycling"
elif season == "Summer":
    if type_of_group == "boys" or type_of_group == "girls":
        accommodation_price = number_of_stays * number_of_students * 15
        if type_of_group == "boys":
            activity = "Football"
        elif type_of_group == "girls":
            activity = "Volleyball"
    elif type_of_group == "mixed":
        accommodation_price = number_of_stays * number_of_students * 20
        activity = "Swimming"

if number_of_students >= 50:
    accommodation_price -= accommodation_price * 0.5
elif 20 <= number_of_students < 50:
    accommodation_price -= accommodation_price * 0.15
elif 10 <= number_of_students < 20:
    accommodation_price -= accommodation_price * 0.05

print(f"{activity} {accommodation_price:.2f} lv.")




