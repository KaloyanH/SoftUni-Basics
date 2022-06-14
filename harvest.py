import math

square_meters = int(input())
grape_per_square_meters = float(input())
needed_liters_wine = int(input())
workers = int(input())

grapes = square_meters * grape_per_square_meters
wine_production = grapes * 0.4
liters_wine = wine_production / 2.5

if liters_wine < needed_liters_wine:
        difference_wine_litters = needed_liters_wine - liters_wine
        print(f'It will be a tough winter! More {math.floor(difference_wine_litters)} liters wine needed.')

elif liters_wine >= needed_liters_wine:
        wine_left = liters_wine - needed_liters_wine
        wine_per_worker = wine_left / workers
        print(f'Good harvest this year! Total wine: {math.floor(liters_wine)} liters.')
        print(f'{math.ceil(wine_left)} liters left -> {math.ceil(wine_per_worker)} liters per person.')



