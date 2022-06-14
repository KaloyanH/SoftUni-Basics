pens = int(input())
markers = int(input())
liters_detergent = int(input())
discount = int(input())

price_of_pens = 5.80
price_of_markers = 7.20
price_of_detergent = 1.2

material_price = pens*price_of_pens + \
    markers*price_of_markers + \
    liters_detergent*price_of_detergent

total_sum = material_price - (material_price*discount/100)

print(total_sum)
