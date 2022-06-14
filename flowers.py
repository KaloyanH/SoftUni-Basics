number_of_Chrysanthemum = int(input())
number_of_roses = int(input())
number_of_tulips = int(input())
season = input()
weekend = input()

price_arranging = 2
price_chrysanthemum = 0
price_roses = 0
price_tulips = 0
sum_bouquet = 0

if season == "Spring" or season == "Summer":
    price_chrysanthemum = 2
    price_roses = 4.10
    price_tulips = 2.50
    sum_bouquet = price_chrysanthemum * number_of_Chrysanthemum + price_roses * number_of_roses + \
                  price_tulips * number_of_tulips
    if weekend == "Y":
        sum_bouquet += sum_bouquet * 0.15
        if number_of_tulips > 7:
            sum_bouquet -= sum_bouquet * 0.05
    if weekend == "N":
        sum_bouquet = sum_bouquet
        if number_of_tulips > 7:
            sum_bouquet -= sum_bouquet * 0.05

elif season == "Autumn" or season == "Winter":
    price_chrysanthemum = 3.75
    price_roses = 4.50
    price_tulips = 4.15
    sum_bouquet = price_chrysanthemum * number_of_Chrysanthemum + price_roses * number_of_roses + \
                  price_tulips * number_of_tulips
    if weekend == "Y":
        sum_bouquet += sum_bouquet * 0.15
        if number_of_roses >= 10 and season == "Winter":
            sum_bouquet -= sum_bouquet * 0.1
    if weekend == "N":
        sum_bouquet = sum_bouquet
        if number_of_roses >= 10 and season == "Winter":
            sum_bouquet -= sum_bouquet * 0.1

number_of_flowers = number_of_Chrysanthemum + number_of_roses + number_of_tulips

if number_of_flowers > 20:
    sum_bouquet -= sum_bouquet * 0.2

total_sum = sum_bouquet + price_arranging

print(f"{total_sum:.2f}")
