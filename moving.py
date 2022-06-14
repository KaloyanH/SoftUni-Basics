width = int(input())
length = int(input())
height = int(input())

free_space = width * length * height
taken_space = 0
command = input()
there_is_free_space = True

while command != "Done":
    boxes = int(command)
    free_space -= boxes
    if free_space < 0:
        there_is_free_space = False
        break
    command = input()
if there_is_free_space:
    print(f"{free_space} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(free_space)} Cubic meters more.")


