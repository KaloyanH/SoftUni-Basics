name_of_actor = input()
academy_points = float(input())
jury = int(input())

overall_points = 0
jury_points = 0
sum_points = 0

for _ in range(1, jury + 1):
    name_of_jury = input()
    points_of_jury = float(input())
    jury_points = len(name_of_jury) * points_of_jury / 2
    overall_points += jury_points
    sum_points = academy_points + overall_points
    if sum_points > 1250.50:
        print(f'Congratulations, {name_of_actor} got a nominee for leading role with {sum_points:.1f}! ')
        break

if sum_points <= 1250.50:
    difference = 1250.50 - sum_points
    print(f"Sorry, {name_of_actor} you need {difference:.1f} more!")

