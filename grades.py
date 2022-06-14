students_attending = int(input())

total_sum_grades = 0
fail_grades = 0
average_grades = 0
good_grades = 0
top_grades = 0

for _ in range(1, students_attending + 1):
    current_grade = float(input())
    if current_grade <= 2.99:
        fail_grades += 1
    elif 3 <= current_grade <= 3.99:
        average_grades += 1
    elif current_grade <= 4.99:
        good_grades += 1
    elif current_grade >= 5:
        top_grades += 1
    total_sum_grades += current_grade

average_grades_total = total_sum_grades / students_attending
percent_fail_grades = fail_grades / students_attending * 100
percent_average_grades = average_grades / students_attending * 100
percent_good_grades = good_grades / students_attending * 100
percent_top_grades = top_grades / students_attending * 100

print(f"Top students: {percent_top_grades:.2f}%")
print(f"Between 4.00 and 4.99: {percent_good_grades:.2f}%")
print(f"Between 3.00 and 3.99: {percent_average_grades:.2f}%")
print(f"Fail: {percent_fail_grades:.2f}%")
print(f"Average: {average_grades_total:.2f}")

