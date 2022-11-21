# Дана квадратная матрица, заполненная случайными числами. 
# Определите, сумма элементов каких строк превосходит 
# сумму главной диагонали матрицы
import random

rows = 5
columns = 5
numbers = [0] * rows

for i in range(len(numbers)):
    numbers[i] = list(random.randint(0, 9) for _ in range(columns))

for row in numbers:
    print(row)

result = sum(numbers[i][j] for i in range(rows) for j in range(columns) if i==j)
print(f'Сумма главной диагонали: {result}')

for row in numbers:
    if sum(row) > result:
        print(f'Сумма элементов строки {row} ({sum(row)}) превосходит сумму главной диагонали')
if sum(row) <= result:
    print('Нет строки, сумма элементов которой превосходит сумму главной диагонали')