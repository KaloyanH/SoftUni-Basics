bad_grades = int(input())

count_bad_grades = 0
grade = 0
name_of_problem = ""
count_of_problems = 0
sum_grades = 0

while name_of_problem != "Enough":
    name_of_problem = input()
    grade = int(input())
    count_of_problems += 1
    sum_grades += grade
    if count_bad_grades == bad_grades:
        break
    if grade <= 4:
        count_bad_grades += 1


average_grade = sum_grades / count_of_problems
if count_bad_grades == bad_grades:
    print(f"You need a break, {count_bad_grades} poor grades.")

else:
    print(f"Average score: {average_grade}")
    print(f"Number of problems: {count_of_problems}")
    print(f"Last problem: {name_of_problem}")
