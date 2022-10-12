# print('hello world')
# типы данных и переменная
# int, float, boolean, str, list, None
# value = None
# print(type(value))

# a = 123
# b = 1.23
# print(type(a))
# print(type(b))
# value = 12334

# s = 'qwert hello' # \n  - переход на новую строку, 
# \... - сохранение символа в строке

# print(s) # вывод строки
# print(a, ' - ' ,b, ' - ', s)
# print('{1} - {2} - {0}'.format(a, b, s)) c указанием индексов
# print(f'{a} - {b} - {s}')

# f = True
# print(f)
# list = ['1', '2', '3', 1, 2, 4.3, 2, True]
# col = ['hello', 3,2,4, True]
# print(list)
# print(col)

# print('Введите a')
# a = int(input())
# print('Введите b')
# b = int(input())
# print(a, b, ' ', a + b) # при сложении получим складывание строк
# поэтому добавляем при получении вводных данных int
# соответственно так же используем float для значений с запятой

# a = 123
# b = 321
# c = a + b
# print(c)
r = range(10)
for i in r:
    print(i)
