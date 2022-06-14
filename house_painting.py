x = float(input())
y = float(input())
h = float(input())


door_area = 1.2*2
window_area = 1.5*1.5
front_back_wall_area = x*x - door_area + x*x
side_walls = 2*(x*y) - 2*window_area

top_roof_area = 2*(x*y)
side_top_roof_area = 2*((x*h)/2)

green_paint = (front_back_wall_area + side_walls) / 3.4
red_paint = (top_roof_area + side_top_roof_area) / 4.3

print(f'{green_paint : .2f}')
print(f'{red_paint : .2f}')



