number_of_groups = int(input())

sum_people = 0
people_for_peek1 = 0
people_for_peek2 = 0
people_for_peek3 = 0
people_for_peek4 = 0
people_for_peek5 = 0

for _ in range(1, number_of_groups+1):
    number_of_people = int(input())
    if number_of_people <= 5:
        people_for_peek1 += number_of_people
    elif 6 <= number_of_people <= 12:
        people_for_peek2 += number_of_people
    elif 13 <= number_of_people <= 25:
        people_for_peek3 += number_of_people
    elif 26 <= number_of_people <= 40:
        people_for_peek4 += number_of_people
    elif number_of_people >= 41:
        people_for_peek5 += number_of_people
    sum_people += number_of_people

peek1 = people_for_peek1 / sum_people * 100
peek2 = people_for_peek2 / sum_people * 100
peek3 = people_for_peek3 / sum_people * 100
peek4 = people_for_peek4 / sum_people * 100
peek5 = people_for_peek5 / sum_people * 100

print(f"{peek1:.2f}%")
print(f"{peek2:.2f}%")
print(f"{peek3:.2f}%")
print(f"{peek4:.2f}%")
print(f"{peek5:.2f}%")