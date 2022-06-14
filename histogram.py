count_of_numvbers = int(input())

first_numbers = 0
second_numbers = 0
third_numbers = 0
fourth_numbers = 0
fifth_numbers = 0

for _ in range(1, count_of_numvbers+1):
    number = int(input())
    if number < 200:
        first_numbers += 1
    elif number < 400:
        second_numbers += 1
    elif number < 600:
        third_numbers += 1
    elif number < 800:
        fourth_numbers += 1
    elif number >= 800:
        fifth_numbers += 1

percent_first_n = (first_numbers / count_of_numvbers * 100)
percent_second_n = (second_numbers / count_of_numvbers * 100)
percent_third_n = (third_numbers / count_of_numvbers * 100)
percent_fourth_n = (fourth_numbers / count_of_numvbers * 100)
percent_fifth_n = (fifth_numbers / count_of_numvbers * 100)

print(f'{percent_first_n:.2f}%')
print(f'{percent_second_n:.2f}%')
print(f'{percent_third_n:.2f}%')
print(f'{percent_fourth_n:.2f}%')
print(f'{percent_fifth_n:.2f}%')




