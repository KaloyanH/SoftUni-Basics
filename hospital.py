period_of_time = int(input())

number_of_doctors = 7
number_visiting_patients = 0
number_attended_patients = 0
number_unattended_patients = 0

for _ in range(1, period_of_time + 1):
    if _ % 3 == 0:
        if number_unattended_patients > number_attended_patients:
            number_of_doctors += 1
    number_visiting_patients = int(input())
    if number_visiting_patients <= number_of_doctors:
        number_attended_patients += number_visiting_patients
    elif number_visiting_patients > number_of_doctors:
        number_unattended_patients += number_visiting_patients - number_of_doctors
        number_attended_patients += number_of_doctors


print(f"Treated patients: {number_attended_patients}.")
print(f"Untreated patients: {number_unattended_patients}.")
