#  Дан двумерный массив. Определите
# номер строки и столбца, в котором находится
# максимальный элемент

# import numpy as np

# def zadacha4():
#     numbers = np.random.randint(500, size=(10, 15))

#     print(numbers)

#     max_i = 0
#     max_j = 0

#     for i in range(numbers.shape[0]):
#         for j in range(numbers.shape[1]):
#             if numbers[i, j] > numbers[max_i, max_j]:
#                 max_i, max_j = i, j

#     print(max_i, max_j)
import random

def printMatrix(numbers):
    for row in numbers:
        print(row)

def zadacha1():
    rows = 4
    columns = 5
    numbers = [0] * rows
    used = []

    for i in range(len(numbers)):
        numbers[i] = list(0 for _ in range(columns))

    for i in range(rows):
        for j in range(columns):
            current_number = random.randint(0, 30)
            while current_number in used:
                current_number = random.randint(0, 30)
            numbers[i][j] = current_number
            used.append(current_number)
    return numbers

def zadacha4():
    numbers = zadacha1()
    printMatrix(numbers)
    result = []
    for row in numbers:
        for el in row:
            result.append(el)

    max1 = max(result)
    print(f"максимум равен {max1}")
    max_index = result.index(max1)
    print(f"его индекс равен {max_index}")
    rows = len(numbers)
    columns = len(numbers[0])
    print(max_index//columns + 1)
    print(max_index%columns + 1)


zadacha4()



