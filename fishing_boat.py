budget = int(input())
season = input()
fishermen = int(input())

boat_rent = 0

if season == "Spring":
    if fishermen <= 6:
        boat_rent = 3000 - 3000*0.1
    elif 7 <= fishermen <= 11:
        boat_rent = 3000 - 3000*0.15
    elif fishermen > 11:
        boat_rent = 3000 - 3000*0.25

elif season == "Summer" or season == 'Autumn':
    if fishermen <= 6:
        boat_rent = 4200 - 4200*0.1
    elif 7 <= fishermen <= 11:
        boat_rent = 4200 - 4200*0.15
    elif fishermen > 11:
        boat_rent = 4200 - 4200*0.25

elif season == "Winter":
    if fishermen <= 6:
        boat_rent = 2600 - 2600*0.1
    elif 7 <= fishermen <= 11:
        boat_rent = 2600 - 2600*0.15
    elif fishermen > 11:
        boat_rent = 2600 - 2600*0.25

if fishermen % 2 == 0 and season != "Autumn":
    boat_rent *= 0.95

sum_difference = abs(budget - boat_rent)

if budget >= boat_rent:
    print(f'Yes! You have {sum_difference:.2f} leva left.')

elif budget < boat_rent:
    print(f'Not enough money! You need {sum_difference:.2f} leva.')