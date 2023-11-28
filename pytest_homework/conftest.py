import random

import pytest


@pytest.fixture(autouse=True)
def age():
    age = random.randint(1, 100)
    print(f'Random age is {age}')
    yield age


@pytest.fixture
def deleting_random_age():
    yield
    print('Deleting random age.... Done')
