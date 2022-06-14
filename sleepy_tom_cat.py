days_off = int(input())

toms_norm = 30000
days_of_year = 365

playing_om_work_days = (days_of_year - days_off) * 63
playing_om_days_off = days_off * 127

play_time = playing_om_work_days + playing_om_days_off

play_time_difference = abs(toms_norm - play_time)

play_time_hours = play_time_difference // 60
play_time_minutes = play_time_difference % 60


if play_time > toms_norm:
    print('Tom will run away')
    print(f'{play_time_hours} hours and {play_time_minutes} minutes more for play')

else:
    print(f'Tom sleeps well')
    print(f'{play_time_hours} hours and {play_time_minutes} minutes less for play')