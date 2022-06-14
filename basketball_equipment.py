training_tax = int(input())

price_of_sneakers = training_tax - (training_tax*0.4)
price_of_outfit = price_of_sneakers - (price_of_sneakers*0.2)
price_of_basketball = price_of_outfit*0.25
price_of_accessories = price_of_basketball*0.2

total_sum = price_of_sneakers + price_of_outfit + \
            price_of_basketball + price_of_accessories + \
            training_tax

print(total_sum)
