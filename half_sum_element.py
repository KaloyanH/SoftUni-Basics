import sys

number = int(input())

max_number = -sys.maxsize
sum_numbers = 0

for _ in range(0, number):
    num = int(input())
    if num > max_number:
        max_number = num
    sum_numbers += num

if max_number == sum_numbers - max_number:
    print("Yes")
    print(f'Sum = {max_number}')

else:
    sum_numbers -= max_number
    print("No")
    print(f"Diff = {abs(sum_numbers-max_number)}")