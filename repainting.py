nylon = int(input())
paint = int(input())
thinner = int(input())
hours_of_work = int(input())

price_of_nylon = 1.5
price_of_paint = 14.50
price_of_thinner = 5
price_of_bags = 0.4

total_sum_materials = ((nylon+2)*price_of_nylon) + \
                      (paint+(paint*0.1))*price_of_paint + \
                      thinner*price_of_thinner + price_of_bags

total_sum_workers = hours_of_work*(total_sum_materials*0.3)

total_sum = total_sum_materials + total_sum_workers

print(total_sum)
