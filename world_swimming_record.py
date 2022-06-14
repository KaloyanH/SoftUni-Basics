record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds = float(input())

overall_time = distance_in_meters * time_in_seconds
added_time = distance_in_meters // 15 * 12.5

sum_time = overall_time + added_time

difference_in_time = abs(sum_time - record_in_seconds)

if sum_time < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {sum_time:.2f} seconds.")

else:
    print(f'No, he failed! He was {difference_in_time:.2f} seconds slower.')