# Программа загадывает случайное число от 0 до 100.
# Пользователь пытается угадать, вводя числа.
# Если пользователь угадал - выведите поздравление и завершите программу.
# Если пользователь не угадал, подскажите ему в в какую сторону идти.
# То есть, если число пользователя слишком большое - выведите “не угадал, число больше загаданного”.
# Если меньше - выведите “не угадал, число меньше загаданного”.

import random
number = random.randint(0, 101)
while True:
    answer = int(input('Guess the number '))
    if answer == number:
        print('Conrats!')
        break
    else:
        if answer > number:
            print('Try again. Your number is bigger ')
            continue
        elif answer < number:
            print('Try again. Your number is smaller ')
            continue
        else:
            print('Congrats')
            break
