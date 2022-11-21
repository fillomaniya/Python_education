# Задайте двумерный массив случайных
# чисел размером 4х5. Случайные числа не должны
# повторяться. Запишите массив в txt-файл
import random

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

    for row in numbers:
        print(row)
    return zadacha1