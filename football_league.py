stadium_capacity = int(input())
count_of_fans = int(input())

position = ""
sector_A = 0
sector_B = 0
sector_V = 0
sector_G = 0

for _ in range(1, count_of_fans + 1):
    position = input()
    if position == "A":
        sector_A += 1
    elif position == "B":
        sector_B += 1
    elif position == "V":
        sector_V += 1
    elif position == "G":
        sector_G += 1

percent_for_A = sector_A / count_of_fans * 100
percent_for_B = sector_B / count_of_fans * 100
percent_for_V = sector_V / count_of_fans * 100
percent_for_G = sector_G / count_of_fans * 100

total_attending = sector_A + sector_B + sector_V + sector_G
overall_percent = total_attending / stadium_capacity * 100

print(f"{percent_for_A:.2f}%")
print(f"{percent_for_B:.2f}%")
print(f"{percent_for_V:.2f}%")
print(f"{percent_for_G:.2f}%")
print(f"{overall_percent:.2f}%")
