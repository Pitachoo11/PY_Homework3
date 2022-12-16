# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

print('Введите количество чисел в списке')
n = int (input())

numbers = []
result = []

for i in range(0, n):
    numbers.append(random.randint(1,10))

for i in range(0, len(numbers) // 2 + len(numbers) % 2):    
        result.append(numbers[i] * numbers[n-i-1])

print(numbers)
print(result)
