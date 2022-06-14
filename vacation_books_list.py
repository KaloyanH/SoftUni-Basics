number_of_pages = int(input())
pages_per_hour = int(input())
days_for_reading = int(input())

hours_of_reading = number_of_pages / pages_per_hour
sum = hours_of_reading // days_for_reading
print(sum)







