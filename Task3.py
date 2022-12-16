# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

print('Введите количество чисел в списке')
n = int (input())

numbers = []
maximum = -1
minimum = 100

for i in range(0, n):
    numbers.append(round(random.uniform(1,20), 2))
    if (numbers[i] % 1) > maximum:
        maximum = numbers[i] % 1
    elif (numbers[i] % 1) < minimum:
        minimum = numbers[i] % 1

print(numbers)
print('Максимум-остаток', round(maximum,2))
print('Минимум-остаток', round(minimum,2))
print('Разница Максимум-Минимум', round(maximum-minimum,2))
