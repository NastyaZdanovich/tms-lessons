import pytest


class TestHomework:
    @pytest.mark.wizard
    @pytest.mark.parametrize('first_name', ['John', 'Harry', 'Ron'])
    @pytest.mark.parametrize('last_name', ['Smith', 'Potter', 'Weasly'])
    def test_fail_if_john_smith(self, age, first_name, last_name, deleting_random_age):
        if first_name == 'John' and last_name == 'Smith':
            pytest.xfail('He is a muggle')
        print(f'Hello, {first_name} {last_name}. Your age is {age}')
