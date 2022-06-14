number_of_loads = int(input())

price_of_load = 0
loads_per_van = 0
loads_per_truck = 0
loads_per_train = 0
total_weight_of_load = 0

for _ in range(1, number_of_loads+1):
    weight_of_load = int(input())
    if weight_of_load <= 3:
        price_of_load += weight_of_load * 200
        loads_per_van += weight_of_load
    elif 4 <= weight_of_load <= 11:
        price_of_load += weight_of_load * 175
        loads_per_truck += weight_of_load
    elif weight_of_load >= 12:
        price_of_load += weight_of_load * 120
        loads_per_train += weight_of_load
    total_weight_of_load += weight_of_load

average_price = price_of_load / total_weight_of_load
percent_per_van = loads_per_van / total_weight_of_load * 100
percent_per_truck = loads_per_truck / total_weight_of_load * 100
percent_per_train = loads_per_train / total_weight_of_load * 100

print(f"{average_price:.2f}")
print(f"{percent_per_van:.2f}%")
print(f"{percent_per_truck:.2f}%")
print(f"{percent_per_train:.2f}%")





