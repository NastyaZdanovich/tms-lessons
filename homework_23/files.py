import json


def read_a_file():
    with open('HW_Files.txt', encoding='utf-8') as file:
        some_list = file.read()
    print(some_list)


def write_json_file():
    with open('my_json_file.json', 'w', encoding='utf-8') as file:
        my_dict = {
            'Рон': 'Уизли',
            'Гермиона': 'Грейнджер',
            'Гарри': 'Поттер'
        }
        json.dump(
            my_dict,
            file,
            ensure_ascii=False,
            indent=4,
            sort_keys=True
        )


def read_json_file():
    with open('my_json_file.json', encoding='utf-8') as file:
        json_contest = json.load(file)
    return json_contest


read_a_file()
write_json_file()
print(read_json_file())
