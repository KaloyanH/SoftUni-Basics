import math

price_skumr = float(input())
price_caca = float(input())
kg_pala = float(input())
kg_safri = float(input())
kg_mussels = int(input())

price_pala = price_skumr + price_skumr*0.6
price_safri = price_caca + price_caca*0.8
price_mussles = 7.5

overall_pala = price_pala*kg_pala
overall_safri = price_safri*kg_safri
overall_mussels = price_mussles*kg_mussels

total_sum = overall_pala + overall_safri + overall_mussels

print(f"{total_sum:.2f}")
