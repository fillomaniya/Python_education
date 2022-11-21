# Считайте двумерный массив из файла.
# Найдите разницу между вторым максимальным и
# вторым минимальным элементами массива
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

def zadacha2():
    numbers = zadacha1()
    printMatrix(numbers)
    result = []

    for row in numbers:
        for el in row:
            result.append(el)
    result.sort()
    print(f'{result[-2]} - {result[1]} = {result[-2] - result[1]}')
zadacha2()


