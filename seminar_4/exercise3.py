# Сгенерируйте список случайных чисел от
# 1 до 20, состоящий из 10 элементов. Удалите из
# списка дубликаты уже имеющихся элементов.

import random

def GetNumbers():
    data = open('python/seminar_4/list.txt', 'w')
    numbers = [random.randint(1, 20) for i in range(10)]
    data.write(str(numbers))
    print(numbers)
    data.close()
GetNumbers()

def FindDuplicate():
    data = open('python/seminar_4/list.txt', 'r')
    num = data.readline()[1:-1].split(", ")
    num = [int(i) for i in num]
    num = set(num)
    num = list(num)
    print(num)
    data.close()
FindDuplicate()
