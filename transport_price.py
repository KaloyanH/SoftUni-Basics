kilometers = int(input())
day_night = input()

if kilometers < 20 and day_night == "day":
    price = kilometers * 0.79 + 0.7
    print(f'{price:.2f}')
elif kilometers < 20 and day_night == 'night':
    price = kilometers * 0.9 + 0.7
    print(f'{price:.2f}')
elif kilometers < 100 and day_night == "day":
    price = kilometers * 0.09
    print(f'{price:.2f}')
elif kilometers < 100 and day_night == "night":
    price = kilometers * 0.09
    print(f'{price:.2f}')
elif kilometers >= 100 and day_night == 'day':
    price = kilometers * 0.06
    print(f'{price:.2f}')
elif kilometers >= 100 and day_night == 'night':
    price = kilometers * 0.06
    print(f'{price:.2f}')