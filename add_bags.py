luggage_above_20_price = float(input())
luggage_kgs = float(input())
days_of_travel = int(input())
luggage_count = int(input())


if days_of_travel < 7 and luggage_kgs < 10:
    luggage_price = luggage_above_20_price * 0.2
    sum_luggage = (luggage_price + (luggage_price * 0.4)) * luggage_count
    print(f'The total price of bags is: {sum_luggage:.2f} lv. ')

elif 7 <= days_of_travel <= 30 and luggage_kgs < 10:
    luggage_price = luggage_above_20_price * 0.2
    sum_luggage = (luggage_price + (luggage_price * 0.15)) * luggage_count
    print(f'The total price of bags is: {sum_luggage:.2f} lv. ')

elif days_of_travel > 30 and luggage_kgs < 10:
    luggage_price = luggage_above_20_price * 0.2
    sum_luggage = (luggage_price + (luggage_price * 0.1)) * luggage_count
    print(f'The total price of bags is: {sum_luggage:.2f} lv. ')

elif days_of_travel < 7 and 10 <= luggage_kgs <= 20:
    luggage_price = luggage_above_20_price * 0.5
    sum_luggage = (luggage_price + (luggage_price * 0.4)) * luggage_count
    print(f'The total price of bags is: {sum_luggage:.2f} lv. ')

elif 7 <= days_of_travel <= 30 and 10 <= luggage_kgs <= 20:
    luggage_price = luggage_above_20_price * 0.5
    sum_luggage = (luggage_price + (luggage_price * 0.15)) * luggage_count
    print(f'The total price of bags is: {sum_luggage:.2f} lv. ')

elif days_of_travel > 30 and 10 <= luggage_kgs <= 20:
    luggage_price = luggage_above_20_price * 0.5
    sum_luggage = (luggage_price + (luggage_price * 0.1)) * luggage_count
    print(f'The total price of bags is: {sum_luggage:.2f} lv. ')

elif days_of_travel < 7 and luggage_kgs > 20:
    luggage_price = luggage_above_20_price
    sum_luggage = (luggage_price + (luggage_price * 0.4)) * luggage_count
    print(f'The total price of bags is: {sum_luggage:.2f} lv. ')

elif 7 <= days_of_travel <= 30 and luggage_kgs > 20:
    luggage_price = luggage_above_20_price
    sum_luggage = (luggage_price + (luggage_price * 0.15)) * luggage_count
    print(f'The total price of bags is: {sum_luggage:.2f} lv. ')

elif days_of_travel > 30 and luggage_kgs > 20:
    luggage_price = luggage_above_20_price
    sum_luggage = (luggage_price + (luggage_price * 0.1)) * luggage_count
    print(f'The total price of bags is: {sum_luggage:.2f} lv. ')






