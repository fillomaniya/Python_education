# Напишите программу, которая принимает 
# на вход число N и выдает список факториалов
#  для чисел от 1 до N. 
# N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
import math

print("Введите число N: ")
N = int(input())
print(f"N = {N} ->", end = " ")
list = []
for i in range(1, N+1):
    res = math.factorial(i)
    list.append (res)
print(list)