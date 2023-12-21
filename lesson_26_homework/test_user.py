import requests
import pytest
import names
from datetime import datetime
import random
import string


class Users:
    HOST = 'https://petstore.swagger.io/v2'
    POST = '/user'  # create
    USER_USERNAME = '/user/{username}'  # read, update, delete


first_name = names.get_first_name(gender='female')
last_name = names.get_last_name()
user_name = f"{first_name.lower()}_{last_name.lower()}"
user_id = int(datetime.now().timestamp())
user_password = ''.join(random.choice(string.ascii_lowercase) for i in range(10))


@pytest.fixture
def user_info():
    data = {
        "id": user_id,
        "username": user_name,
        "firstName": first_name,
        "lastName": last_name,
        "email": "string",
        "password": user_password,
        "phone": "string",
        "userStatus": 0
    }
    return data


def check_response(response):
    assert response.ok, f'{response.status_code =}'


def create_user(user_info):
    url = f'{Users.HOST}{Users.POST}'
    response = requests.post(url, json=user_info)
    return response


def read_user(user_info):
    url = f'{Users.HOST}{Users.USER_USERNAME.format(username=user_info["username"])}'
    response = requests.get(url)
    return response


def update_user(user_info, json_data):
    url = f'{Users.HOST}{Users.USER_USERNAME.format(username=user_info["username"])}'
    response = requests.put(url, json=json_data)
    return response


def delete_user(user_info):
    url = f'{Users.HOST}{Users.USER_USERNAME.format(username=user_info["username"])}'
    response = requests.delete(url)
    return response


def check_message(response, expected_message):
    json_data = response.json()
    assert json_data["message"] == str(expected_message), f'{json_data["message"] = }'


def check_user_name(response, expected_user_name):
    json_data = response.json()
    assert json_data["username"] == expected_user_name, f'{json_data["username"] = }'


def check_full_name(response, expected_first_name, expected_last_name):
    json_data = response.json()
    assert json_data["firstName"] == expected_first_name, f'{json_data["firstName"] = }'
    assert json_data["lastName"] == expected_last_name, f'{json_data["lastName"] = }'


class TestClassUser:

    def test_create_user(self, user_info):
        create_user_response = create_user(user_info)
        check_response(create_user_response)
        check_message(create_user_response, user_info["id"])
        ...

    def test_read_user(self, user_info):
        create_user_response = create_user(user_info)
        check_response(create_user_response)
        check_message(create_user_response, user_info["id"])

        read_user_response = read_user(user_info)
        check_response(read_user_response)
        check_user_name(read_user_response, user_info["username"])

    def test_update_user(self, user_info):
        create_user_response = create_user(user_info)
        check_response(create_user_response)
        check_message(create_user_response, user_info["id"])

        read_user_response = read_user(user_info)
        check_response(read_user_response)
        check_user_name(read_user_response, user_info["username"])
        check_full_name(read_user_response, user_info["firstName"], user_info["lastName"])

        json_data = read_user_response.json()
        first_name_new = 'Elena'
        last_name_new = 'Smith'
        json_data["firstName"] = first_name_new
        json_data["lastName"] = last_name_new
        update_user_response = update_user(user_info, json_data=json_data)
        check_response(update_user_response)

        read_updated_user_response = read_user(user_info)
        check_response(read_updated_user_response)
        check_full_name(read_updated_user_response, first_name_new, last_name_new)
        ...

    def test_delete_user(self, user_info):
        create_user_response = create_user(user_info)
        check_response(create_user_response)
        check_message(create_user_response, user_info["id"])

        read_user_response = read_user(user_info)
        check_response(read_user_response)
        check_user_name(read_user_response, user_info["username"])

        delete_user_response = delete_user(user_info)
        check_response(delete_user_response)
        check_message(delete_user_response, user_info["username"])

        read_deleted_user_response = read_user(user_info)
        check_message(read_deleted_user_response, "User not found")




















