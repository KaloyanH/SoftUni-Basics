budget = float(input())
season = input()

expenses = 0
destination = ''
type_of_vacation = ''

if budget <= 100:
    if season == "summer":
        expenses = budget*0.3
        destination = "Bulgaria"
        type_of_vacation = "Camp"
    elif season == "winter":
        expenses = budget*0.7
        destination = "Bulgaria"
        type_of_vacation = "Hotel"

elif 100 < budget <= 1000:
    if season == 'summer':
        expenses = budget*0.4
        destination = 'Balkans'
        type_of_vacation = 'Camp'
    elif season == "winter":
        expenses = budget*0.8
        destination = 'Balkans'
        type_of_vacation = "Hotel"

elif budget > 1000:
    expenses = budget*0.9
    destination = "Europe"
    type_of_vacation = "Hotel"

print(f'Somewhere in {destination}')
print(f'{type_of_vacation} - {expenses:.2f}')




