# Решите прошлую задачу так, чтобы ваш декоратор работал
# для любой функции, с любым количеством параметров.
# А также чтобы работало с именованными параметрами.
# Подсказка: используйте *args и **kwargs.


def my_decorator(func):
    def inner(*args, **kwargs):
        print(f'Функция получила на вход значение {args, kwargs}')
        # объясните,пожалуйста,на лекции,почему не работает со звездочками
        print(f'Результат функции {func(*args, **kwargs)}')
        return func(*args, **kwargs)
    return inner


@my_decorator
def my_func(a, b, c, d):
    return a + b + c + d


y = my_func(1, 2, d=3, c=4)
print(f'y = {y}')
