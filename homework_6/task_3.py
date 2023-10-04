# Решите прошлую задачу, в которой теперь пользователь может вводить буквы в любом регистре.
# Вам по прежнему нужно удалить все гласные. При этом вывести результат нужно, сохранив изначальный регистр.


def remove_vowels():
    return list(input('Введите латинские буквы: ').split())


my_list = remove_vowels()
vowels = 'aeiouAEIOU'
no_vowels = list(filter(lambda s: s not in vowels, my_list))
print(f'Строка без гласных: {no_vowels}')

