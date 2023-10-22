# 1. Создайте файл person.py, делайте задание в этом файле.
# 2. Создайте класс Person. У класса должно быть три поля: full_name, age, gender,
# которые должны заполняться в конструкторе.
# Будем считать что поле gender имеет тип str и может быть либо 'M' (male), либо 'F' (female).
# 3. Добавьте в класс метод print_person_info, который печатает на экран строку:
# "Person: {full_name} ({gender}), {age} years old"
# 4. Добавьте метод get_birth_year, которая возвращает год рождения человека (рассчитанное как 2023 - age)
# * Замените цифру 2023 на текущий год (чтобы ваша программа работала правильно даже через год).
# Текущий год можно взять с помощью модуля datetime (пример).

import datetime


class Person:
    def __init__(self, full_name, age, gender):
        self.full_name = full_name
        self.age = age
        self.gender = gender

    def print_person_info(self):
        return f'Person: {self.full_name}, {self.gender}, {self.age} years old'

    # def get_birth_year(self):
        #return f'Birth year: {2023 - self.age}'

    def get_birth_year_precisely(self):
        x = datetime.datetime.now()
        return f'Birth year: {x.year - self.age}'


p = Person('Nastya Zdanovich', 27, 'F(female)')
print(p.print_person_info())
# print(p.get_birth_year())
print(p.get_birth_year_precisely())
