# Напишите функцию get_longest_word, которая на вход
# принимает текст (только английские слова и пробелы), и
# возвращает самое длинное слово из этого текста.
def get_longest_word(string):
    max_el = max(string.split(), key=len)
    return max_el


print(get_longest_word('get longest word'))
print(get_longest_word('process finished with exit code'))
print(get_longest_word('hello this is a string with words and spaces and big big woooooooooord'))
