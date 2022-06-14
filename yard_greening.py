square_meters = float(input())

price_for_square_meter = 7.61

overall_price = square_meters*price_for_square_meter
discount = overall_price*0.18

total_cost = overall_price - discount

print(f'The final price is: {total_cost} lv.')
print(f"The discount is: {discount} lv.")







