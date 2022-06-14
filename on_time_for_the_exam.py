hour_of_exam = int(input())
minute_of_exam = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())

time_of_exam = hour_of_exam * 60 + minute_of_exam
time_of_arrival = hour_of_arrival * 60 + minute_of_arrival
time_difference = time_of_exam - time_of_arrival

if 0 <= time_difference <= 30:
    if time_difference == 0:
        print("On time")
    else:
        print("On time")
        print(f"{time_difference} minutes before the start")
elif time_difference > 30:
    if time_difference < 60:
        print("Early")
        print(f"{time_difference} minutes before the start")
    elif time_difference >= 60:
        print("Early")
        print(f"{time_difference // 60}:{time_difference % 60:02d} hours before the start")
else:
    print("Late")
    if abs(time_difference) < 60:
        print(f"{abs(time_difference)} minutes after the start")
    else:
        print(f"{abs(time_difference) // 60}:{abs(time_difference) % 60:02d} hours after the start")








