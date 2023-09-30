# Напишите функцию is_year_leap, которая принимает число (год) и возвращает True если год високосный
def is_year_leap(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


assert(is_year_leap(2000))
assert(is_year_leap(1984))
