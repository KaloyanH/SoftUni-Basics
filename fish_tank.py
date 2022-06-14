length_in_cm = int(input())
width_in_cm = int(input())
heigth_in_cm = int(input())
percent = float(input())

aquarium_volume = length_in_cm*width_in_cm*heigth_in_cm
aquarium_litres = aquarium_volume*0.001

total_litres = aquarium_litres - (aquarium_litres*percent/100)

print(total_litres)
