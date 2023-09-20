number = int(input('Введите число: '))
count = 0
for i in range(1, number+1):
    if number % i == 0:
        count += 1
print(count == 2)
