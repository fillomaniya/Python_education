# Дано число N. Найти все его делители.
# Для каждого делителя укажите четный он или нечетный

# def CheckEven(x):
#     if x % 2 == 0:
#         return " - четный"
#     else:
#         return " - нечетный"

# def Zadacha0(number):
#     for i in range (1, number + 1):
#         if number % i == 0:
#             print(i, end = " ")
#             print(CheckEven(i))

# def Test(number):
#     number += 1
#     print(" это печать из метода", number)

# number = 60
# Test(number)
# print("печать вне метода", number)
# __________________________________________

# Выведите таблицу истинности для выражения - (не) X v (или) Y

# print("x | y | res")
# for x in range(0,2):
#     for y in range(0,2):
#         F = not x or y
#         print(f"{x} | {y} | {int(F)}")
# __________________________________________

# Напишите программу, в которой 
# пользователь будет задавать две строки, 
# а программа - определять количество 
# вхождений одной строки в другую

# string_1 = input()
# string_2 = input()
# count = 0
# if len(string_1) > len(string_2):
#     print(string_1)
#     for i in range (len(string_1)):
#         print(string_1[i : i + len(string_2)])
#         if string_2 == string_1[i : i + len(string_2)]:
#             count += 1
#     print("количество совпадений строк: ", count)
# else:
#     print(string_2)

# Решение с готовым методом из языка count:

# str1 = input('Enter text1: ')
# str2 = input('Enter text2: ')
# print(f'text1 include text2 {str1.count(str2)} times(s)')

# ___________________________________________

# Дано число N. Заполните список длиной N
# элементами 1, -3, 9, -27, 81, -243...

# N = int(input())
# list = []
# n = -3
# for i in range (0, N):
#     list.append(n**i)
# print(list)
# ___________________________________________

# Найти все числа до 10000, 
# у которого количество делителей равно 10

 

