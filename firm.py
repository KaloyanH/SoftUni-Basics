import math

needed_hours = int(input())
days = int(input())
overtime_workers = int(input())

working_days = days - days * 0.1
working_hours = working_days * 8
overtime_hours = overtime_workers * 2 * days

overall_hours =  working_hours + overtime_hours

if overall_hours >= needed_hours:
    time_left = overall_hours - math.floor(needed_hours)
    print(f'Yes!{math.floor(time_left)} hours left.')
else:
    time_left = needed_hours - math.floor(overall_hours)
    print(f'Not enough time!{time_left} hours needed.')



