# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

print('Введите количество чисел в списке')
n = int(input())

summ = 0
list = []

for i in range(0, n):
    list.append(random.randint(1,10))
    if i % 2 == 0:
        summ += list[i]
print(list)
print('Cумма элементов списка, стоящих на нечётных позициях = ', summ)