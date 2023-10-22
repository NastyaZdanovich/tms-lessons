# Создайте файл point.py. Делайте задание в этом файле.
# Вам необходимо создать класс Point (точка на координатной плоскости), у которой будет два поля: x, y.
# Добавьте метод distance_to_zero - который будет возвращать расстояние от точки до начала координат (0, 0).
# Например для точки Point(3, 4) это расстояние будет равно 5 (по теореме Пифагора)
# Добавьте метод distance_to_point, который принимает другую точку, и ищет расстояние между ними.
# Скопируйте код из комментария к слайду и проверьте, что он выводит ожидаемый результат.


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_zero(self):
        return f'Расстояние от точки до начала координат: {(self.x ** 2 + self.y ** 2) ** 0.5}'

    def distance_to_point(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5


p1 = Point(3, 4)
p2 = Point(3, 10)
p3 = Point(10, 10)
print(p1.distance_to_zero())
print(p2.distance_to_zero())
print(p3.distance_to_zero())
print('Расстояние между точками p1 и p1:', p1.distance_to_point(p1))
print('Расстояние между точками p1 и p2:', p1.distance_to_point(p2))
print('Расстояние между точками p2 и p1:', p2.distance_to_point(p1))
print('Расстояние между точками p1 и p3:', p1.distance_to_point(p3))
print('Расстояние между точками p2 и p3:', p2.distance_to_point(p3))
