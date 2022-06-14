

name = input()
adult_tickets = int(input())
children_tickets = int(input())
price_adult_tickets = float(input())
service_tax = float (input())

price_children_tickets = price_adult_tickets * 0.3

adult_sum_tickets = adult_tickets * (price_adult_tickets + service_tax)
child_sum_tickets = children_tickets * (price_children_tickets + service_tax)

profit = (adult_sum_tickets + child_sum_tickets) * 0.2

print(f'The profit of your agency from {name} tickets is {profit:.2f} lv.')

