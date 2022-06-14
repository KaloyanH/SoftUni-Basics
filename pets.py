import math

days = int(input())
food = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input())

dog_food = days * dog_food_per_day
cat_food = days * cat_food_per_day
turtle_food = days * turtle_food_per_day / 1000

food_needed = dog_food + cat_food + turtle_food

if food_needed <= food:
    food_left = food - food_needed
    print(f'{math.floor(food_left)} kilos of food left.')

else:
    food_left = food_needed - food
    print(f'{math.ceil(food_left)} more kilos of food are needed.')
