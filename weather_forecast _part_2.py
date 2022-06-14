a = float(input())

if 26 <= a and a <= 35:
    print("Hot")
elif 20.1 <= a and a <= 25.90:
    print('Warm')
elif 15<= a and a <= 20:
    print('Mild')
elif 12 <= a and a <= 14.9:
    print('Cool')
elif 5 <= a and a <= 11.9:
    print('Cold')

else:
    print('unknown')


