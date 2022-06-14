volume = int(input())
pipe_1 = int(input())
pipe_2 = int(input())
hours = float(input())

debit_pipe_1 = pipe_1 * hours
debit_pipe_2 = pipe_2 * hours

sum_debit = debit_pipe_1 + debit_pipe_2

percent_debit = sum_debit / volume * 100
percent_pipe_1 = debit_pipe_1 / sum_debit * 100
percent_pipe_2 = debit_pipe_2 / sum_debit * 100

difference_volume_debit = abs(volume - sum_debit)

if volume >= sum_debit:
    print(f'The pool is {percent_debit:.2f}% full. Pipe 1: {percent_pipe_1:.2f}%. Pipe 2: {percent_pipe_2:.2f}%.')
else:
    print(f'For {hours} hours the pool overflows with {difference_volume_debit} liters.')





