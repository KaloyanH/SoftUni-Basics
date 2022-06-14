change = float(input())
change = int(change * 100)
number_of_coins = 0

number_of_coins += change // 200
change %= 200
number_of_coins += change // 100
change %= 100
number_of_coins += change // 50
change %= 50
number_of_coins += change // 20
change %= 20
number_of_coins += change // 10
change %= 10
number_of_coins += change // 5
change %= 5
number_of_coins += change // 2
change %= 2
number_of_coins += change // 1
change %= 1

print(number_of_coins)

