import math

number_of_tourneys = int(input())
starting_points = int(input())

final_points = 0
wins = 0

for _ in range(1, number_of_tourneys+1):
    position = input()
    if position == "W":
        final_points += 2000
        wins += 1
    elif position == "F":
        final_points += 1200
    elif position == "SF":
        final_points += 720

average_points = final_points / number_of_tourneys
percentage = wins / number_of_tourneys * 100
final_points += starting_points
print(f"Final points: {math.floor(final_points)}")
print(f"Average points: {math.floor(average_points)}")
print(f"{percentage:.2f}%")
