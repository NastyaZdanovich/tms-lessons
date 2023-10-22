# Создайте файл friends.py. Делайте задание в этом файле.
# Импортируйте класс Person из первого задания
# from person import Person
# Создайте переменную my_friends - список из объектов класса Person.
# Добавьте в него некоторое количество вымышленных друзей с разными именами, возрастом и полом.
# Выведите информацию о каждом друге на экран.
# Найдите среди друзей самого старшего, выведите информацию о нём на экран.
# Выведите на экран информацию о всех друзьях мужского пола (можно использовать функцию filter, либо генератор списков).
# Заверните код из пунктов 5 и 6 в функции get_oldest_person и filter_male_person соответственно


from person import Person

my_friends = [Person('Ivan Ivanov', 27, 'M'),
              Person('Katya Zimina', 35, 'F'),
              Person('Oleg Pyotrov', 31, 'M')]


def get_the_oldest(lst):
    the_oldest = lst[0]
    for person in lst:
        if person.age > the_oldest.age:
            the_oldest = person
    return the_oldest


def get_male_friends(lst):
    return [friend for friend in lst if friend.gender == 'M']


for i in my_friends:
    print(f'My friend {i.print_person_info()}')


oldest_friend = get_the_oldest(my_friends)
print(f'The oldest friend {oldest_friend.print_person_info()}')


male_friends = get_male_friends(my_friends)
for male in male_friends:
    print(f'Male friend {male.print_person_info()}')
