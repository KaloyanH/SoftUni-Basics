name = input()

is_fruit = name == 'banana' or name == 'apple' or name == 'kiwi' or name == 'cherry' or name == 'lemon' or name == 'grapes'
is_vegetable = name == 'tomato' or name == 'cucumber' or name == 'pepper' or name == 'carrot'

if is_fruit:
    print('fruit')
elif is_vegetable:
    print('vegetable')
else:
    print('unknown')