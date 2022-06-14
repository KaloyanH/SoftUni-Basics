deposited_sum = float(input())
time_of_deposit = int(input())
interest_rate = float(input())

sum = deposited_sum + time_of_deposit * ((deposited_sum * interest_rate / 100) / 12)

print(sum)
