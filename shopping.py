budget = float(input())
gpus = int(input())
cpus = int(input())
ram = int(input())

gpu_price = 250
gpu_sum = gpus * gpu_price
cpu_price = gpu_sum * 0.35
cpu_sum = cpus * cpu_price
ram_price = gpu_sum * 0.1
ram_sum = ram * ram_price

total_sum = gpu_sum + cpu_sum + ram_sum

if gpus > cpus :
    total_sum -= total_sum * 0.15

difference = abs(total_sum - budget)

if budget >= total_sum :
    print(f"You have {difference:.2f} leva left!")

else:
    print(f'Not enough money! You need {difference:.2f} leva more!')