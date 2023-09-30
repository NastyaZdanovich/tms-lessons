# Напишите функцию get_most_frequent_word, которая на вход
# принимает текст (только английские слова и пробелы), и
# возвращает самое часто встречающееся слово. Если таких
# слов несколько - верните любое.


def get_most_frequent_word(string):
    words = {}
    for el in string.split():
        if el in words:
            words[el] += 1
        else:
            words[el] = 1
    most_frequent_word = max(words, key=words.get)
    return most_frequent_word


print(get_most_frequent_word('and me and you and him'))
print(get_most_frequent_word('tomorrow and tomorrow'))
