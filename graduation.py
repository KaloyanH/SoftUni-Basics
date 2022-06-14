student_name = input()

years_of_study = 1
average_grade = 0
sum_grades = 0
fail_terms = 0

while years_of_study <= 12:
    if fail_terms >= 2:
        break
    grade = float(input())
    if grade < 4:
        fail_terms += 1
        continue
    sum_grades += grade
    years_of_study += 1

average_grade = sum_grades / 12

if fail_terms >= 2:
    print(f"{student_name} has been excluded at {years_of_study} grade")
else:
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")





