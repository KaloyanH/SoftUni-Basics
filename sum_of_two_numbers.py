start_int = int(input())
end_int = int(input())
magic_number = int(input())

flag = False
count = 0
for i in range(start_int, end_int +1):
    for _ in range(start_int, end_int +1):
        count += 1
        if i + _ == magic_number:
            print()
            print(f"Combination N:{count} ({i} + {_} = {i + _})")
            flag = True
            break
    if flag:
        break
if not flag:
    print(f"{count} combinations - neither equals {magic_number}")