month = input('Введите название месяца: ')
date = int(input('Введите дату: '))
months = {'january': 31, 'february': 28, 'march': 31, 'april': 30, 'may': 31, 'june': 30, 'july': 31, 'august': 31,
          'september': 30, 'october': 31, 'november': 30, 'december': 31}
days_number = months.get(month)
print(1 <= date <= days_number)
