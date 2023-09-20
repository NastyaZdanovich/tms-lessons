square_side = int(input('Введите длину стороны квадрата: '))
perimeter = square_side * 4
area = square_side ** 2
diagonal = 2 ** 0.5 * square_side
results = (perimeter, area, diagonal)
tuple_a = tuple(results)
print(tuple_a)
