cake_width = int(input())
cake_lenght = int(input())

cake_size = cake_lenght * cake_width
cake_is_over = False
total_pieces = 0
command = input()

while command != "STOP":
    pieces_taken = int(command)
    total_pieces += pieces_taken
    if total_pieces > cake_size:
        difference = abs(total_pieces - cake_size)
        cake_is_over = True
        break

    command = input()

if cake_is_over:
    print(f"No more cake left! You need {difference} pieces more.")
else:
    print(f"{abs(total_pieces)} pieces are left.")