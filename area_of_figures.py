import  math

figure = input()
side_a = float(input())

if figure == "square":
    area_of_square = side_a * side_a
    print(f'{area_of_square:.3f}')

elif figure == "rectangle":
    side_b = float(input())
    area_of_rectangle = side_a * side_b
    print(f'{area_of_rectangle:.3f}')

elif figure == "circle":
    area_of_circle = math.pi * side_a * side_a
    print(f'{area_of_circle:.3f}')

elif figure == "triangle":
    side_c = float(input())
    area_of_triangle = side_a * side_c / 2
    print(f'{area_of_triangle:.3f}')

