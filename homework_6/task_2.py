# Пользователь вводит произвольное количество маленьких латинских букв через пробел.
# Напишите функцию remove_vowels, которая принимает список из этих букв и удаляет из него все гласные буквы.
# Выведите результат работы на экран.

def remove_vowels():
    return list(input('Введите латинские буквы: ').split())


my_list = remove_vowels()
vowels = 'aeiou'
no_vowels = list(filter(lambda s: s not in vowels, my_list))
print(f'Строка без гласных: {no_vowels}')
