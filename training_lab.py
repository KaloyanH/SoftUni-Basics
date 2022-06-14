w = float(input())
h = float(input())

overall_h = (h-1) // 0.7
overall_w = w//1.2

number_of_seats = overall_w*overall_h -3

print(number_of_seats)