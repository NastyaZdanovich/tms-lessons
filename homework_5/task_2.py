# Напишите функцию generate_natural_cubes(n), которая принимает число n и
# возвращает список, состоящий из кубов первых n натуральных чисел.

def generate_natural_cubes(n):
    return [i ** 3 for i in range(1, n + 1)]


assert(generate_natural_cubes(4)) == [1, 8, 27, 64]
assert(generate_natural_cubes(5)) == [1, 8, 27, 64, 125]
