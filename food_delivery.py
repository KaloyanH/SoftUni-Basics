chicken_menus = int(input())
fish_menus = int(input())
vegetarian_menus = int(input())

price_chicken_menu = 10.35
price_fish_menu = 12.40
price_vegetarian_menu = 8.15
delivery = 2.50

price_of_menus = chicken_menus*price_chicken_menu + \
                fish_menus*price_fish_menu + \
                vegetarian_menus*price_vegetarian_menu

dessert = price_of_menus*0.2

total_bill = price_of_menus + dessert + delivery

print(total_bill)


