# Сделайте предыдущую задачу, добавив проверку на корректность ответа пользователя.
# Если он ответил “yes” - завершите программу.
# Если он ответил “no” - продолжайте - продолжайте вывод чисел.
# Если что-то другое - напечатайте "Don't understand you" и продолжайте спрашивать до тех пор, пока ответ не будет корректным.

for number in range(1, 100):
    print(number)
    answer = input('Should we break? ').lower()
    if answer == 'yes':
        break
    elif answer == 'no':
        continue
    else:
        while True:
            print("Don't understand")
            answer = input('Should we break? ').lower()
            if answer == 'no' or answer == 'yes':
                break
        if answer == 'yes':
            break
        elif answer == 'no':
            continue
