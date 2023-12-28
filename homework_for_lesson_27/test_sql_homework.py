from homework_for_lesson_27.data import TABLE_NAME, Person, birth_year


def find_what_you_need(cursor, sql_request):
    rows = cursor.execute(sql_request).fetchall()
    people = [Person(*row) for row in rows]
    return people


class TestDataBase:
    def test_born_in_1980(self, create_database, cursor):
        born_in_1980 = find_what_you_need(cursor, f"SELECT * FROM {TABLE_NAME} WHERE born = 1980")

        for person in born_in_1980:
            assert person.born == 1980
            print(f"Born in 1980: {person.first_name} {person.last_name}")

    def test_the_oldest(self, create_database, cursor):
        the_oldest = find_what_you_need(cursor, f"SELECT * FROM {TABLE_NAME} ORDER BY born  LIMIT 1")
        for person in the_oldest:
            assert person.born == min(birth_year)
            print(f'The oldest is {person.first_name} {person.last_name}')

    def test_born_not_in_1980(self, create_database, cursor):
        not_born_in_1980 = find_what_you_need(cursor, f"SELECT * FROM {TABLE_NAME} WHERE born != 1980")

        for person in not_born_in_1980:
            assert person.born != 1980
            print(f"Not born in 1980: {person.first_name} {person.last_name}")

    def test_blood_status(self, create_database, cursor):
        not_pure_blood = find_what_you_need(cursor, f"SELECT * FROM {TABLE_NAME} WHERE blood_status != 'Pure-blood'")

        for person in not_pure_blood:
            assert person.blood_status != 'Pure-blood'
            print(f"Not pure-blood {person.first_name} {person.last_name}")

