# Создайте файл university.py. Делайте задание в этом файле.
# Импортируйте класс Student из первого задания
# from student import Student
# Создайте переменную students - список объектов класса Student, с разными именами и средней оценкой.
# Посчитайте суммарную стипендию для всех студентов.
# Посчитайте количество отличников (используйте метод is_excellent).
# Заверните код для пунктов 4 и 5 к функции calc_sum_scholarship и get_excellent_student_count

from student import Student


students = [
    Student('Ivan Ivanov', 9),
    Student('Nikolay Petrov', 4),
    Student('Anna Kovalyova', 7),
    Student('Nikita Zaitsev', 5)
]


def calc_sum_scholarship(lst):
    summa = 0
    for student in lst:
        summa += student.get_scholarship()
    return summa


def get_excellent_students_count(lst):
    count = 0
    for student in lst:
        count += student.is_excellent()
    return count


total = calc_sum_scholarship(students)
print(f'Сумма стипендий всех студентов: {total} рублей')

excellent_students = get_excellent_students_count(students)
print(f'Количество отличников: {excellent_students}')

