months = int(input())

water_bill = 20
internet_bill = 15
total_other_bills = 0
total_electricity = 0
for _ in range(1, months+1):
    electricity = float(input())
    other_bills = water_bill + internet_bill + electricity
    total_other_bills += other_bills + other_bills*0.2
    total_electricity += electricity


sum_water = water_bill * months
sum_internet = internet_bill * months


average_bill = (total_electricity + sum_water + sum_internet + total_other_bills) / months

print(f"Electricity: {total_electricity:.2f} lv")
print(f"Water: {sum_water:.2f} lv")
print(f"Internet: {sum_internet:.2f} lv")
print(f"Other: {total_other_bills:.2f} lv")
print(f"Average: {average_bill:.2f} lv")