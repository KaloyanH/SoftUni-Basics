turns = int(input())

range1 = 0
range2 = 0
range3 = 0
range4 = 0
range5 = 0
total_points = 0
invalid_numbers = 0
sum_points = 0
for _ in range(1, turns+1):
    number = int(input())
    if 0 <= number <= 9:
        range1 += 1
        sum_points = number * 0.2
    elif 10 <= number <= 19:
        range2 += 1
        sum_points = number * 0.3
    elif 20 <= number <= 29:
        range3 += 1
        sum_points = number * 0.4
    elif 30 <= number <= 39:
        range4 += 1
        sum_points = 50
    elif 40 <= number <= 50:
        range5 += 1
        sum_points = 100
    if number < 0 or number > 50:
        invalid_numbers += 1
        total_points /= 2
        continue
    total_points += sum_points

percent_range1 = range1 / turns * 100
percent_range2 = range2 / turns * 100
percent_range3 = range3 / turns * 100
percent_range4 = range4 / turns * 100
percent_range5 = range5 / turns * 100
percent_invalid = invalid_numbers / turns * 100

print(f"{total_points:.2f}")
print(f"From 0 to 9: {percent_range1:.2f}%")
print(f"From 10 to 19: {percent_range2:.2f}%")
print(f"From 20 to 29: {percent_range3:.2f}%")
print(f"From 30 to 39: {percent_range4:.2f}%")
print(f"From 40 to 50: {percent_range5:.2f}%")
print(f"Invalid numbers: {percent_invalid:.2f}%")