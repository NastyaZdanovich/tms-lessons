# Напишите функцию generate_squares, которая принимает
# произвольное количество аргументов и возвращает список,
# состоящий из их квадратов.

def generate_square(*args):
    sq_l = []
    for i in args:
        sq_l.append(i**2)
    return sq_l


assert(generate_square(1, 5, 6, 3)) == [1, 25, 36, 9]
