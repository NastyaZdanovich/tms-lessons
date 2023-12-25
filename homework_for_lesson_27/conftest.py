import sqlite3

import pytest

from homework_for_lesson_27.data import DB_NAME, TABLE_NAME, data


@pytest.fixture
def create_database():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute(
        f"create table if not exists {TABLE_NAME}("
        "first_name text, "
        "last_name text, "
        "blood_status text, "
        "born int"");")
    connection.commit()
    cursor.executemany(f"INSERT INTO {TABLE_NAME} (first_name, last_name, blood_status, born) VALUES (?, ?, ?, ?)", data)
    connection.commit()
    yield connection
    cursor.execute(f'DROP TABLE {TABLE_NAME}')
    connection.close()


@pytest.fixture
def cursor(create_database):
    connection = create_database
    cursor = connection.cursor()
    yield cursor
    cursor.close()







