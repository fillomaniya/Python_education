# Создайте файл. Запишите в него i первых элементов 
# последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8
import sys

N = int(input('Введите N: '))
f1 = f2 = 1 

sys.stdout = open("python/seminar_3/fibonacci.txt", "w") 

print(f'{N} ->', f1, f2, end = ' ')
for i in range(2, N):
    f1, f2 = f2, f1 + f2
    print(f2, end=' ') 

sys.stdout.close()
# ответ записывается сразу в текстовый файл, не выводя в консоль