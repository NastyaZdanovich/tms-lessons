# Пользователь вводит произвольное число. Посчитайте сумму цифр этого числа используя операторы % и //

num = int(input('Введите число: '))
num = abs(num)
while True:
    if num < 10:
        print('Это не число, а цифра')
        num = int(input('Введите число: '))
    else:
        break
summa = 0
while num != 0:
    rem = num % 10
    summa += rem
    num = num // 10
print(f'Сумма цифр числа = {summa}')
