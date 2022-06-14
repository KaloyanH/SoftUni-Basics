import math

name_of_series = input()
length_of_series = int(input())
length_of_break = int(input())

time_for_lunch = length_of_break * 0.125
time_for_rest = length_of_break * 0.25

time_left = length_of_break - time_for_lunch - \
            time_for_rest

time_difference = abs(length_of_series-time_left)

if time_left >= length_of_series:
    print(f"You have enough time to watch {name_of_series} and left with {math.ceil(time_difference)} minutes free time.")

else:
    print(f"You don't have enough time to watch {name_of_series}, you need {math.ceil(time_difference)} more minutes.")