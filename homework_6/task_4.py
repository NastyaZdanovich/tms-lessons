# Пользователь вводит произвольное количество слов через пробел.
# #Затем (на следующей строке) вводит один символ (разделитель).
# Вам нужно написать функцию my_join, которая принимает список из строк и символ-разделить,
# и возвращает строку, в которой все слова из списка соединены через символ разделитель.

from functools import reduce
my_words = input('Введите слова: ').split()
my_symbol = input('Введите разделитель: ')


def my_join(my_words, my_symbol):
    return reduce(lambda x, y: x + my_symbol + y, my_words)


new_string = my_join(my_words, my_symbol)
print(f'Строка с разъединителем: {new_string}')
