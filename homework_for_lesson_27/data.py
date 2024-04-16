from dataclasses import dataclass


DB_NAME = 'my_database.db'
TABLE_NAME = 'Gryffindor'


@dataclass
class Person:
    first_name: str
    last_name: str
    blood_status: str
    born: int


data = [('Harry', 'Potter', 'Half-blood', 1980),
        ('Ronald', 'Weasly', 'Pure-blood', 1979),
        ('Hermione', 'Granger', 'Muggle-born', 1980),
        ('Neville', 'Longbottom', 'Pure-blood', 1980),
        ('Rubeus', 'Hagrid', 'Half-breed', 1928)]

birth_year = [j for i in data for j in i if type(j) is int]
