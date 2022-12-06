# Имеются данные о площади и стоимости 15 домов.
# Риелтору требуется узнать в каких домах стоимость 
# квадратного метра меньше 50000 рублей.
# Предоставьте ему графические данные о стоимости 
# квадратного метра каждого дома и список подходящих 
# ему домов, отсортированных по площади.
# Данные о домах сформируйте случайным образом. 
# Площади от 100 до 300 кв. метров, цены от 3 до 20 млн

import matplotlib.pyplot as plt
from random import randint as rt

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

squares = []
for i in range(15):
    squares.append(rt(100, 301))
print(f'Площади домов: {squares}')

prices = []
for i in range(15):
    prices.append(rt(3000000, 20000001))
print(f'Цены домов: {prices}')

metres = []
for i in range(15):
    result = prices[i] / squares[i]
    metres.append(round(result, 2))
print(f'Стоимость квадратного метра каждого дома: {metres}')
plt.bar(numbers, metres)
plt.xlabel('порядковый номер дома')
plt.ylabel('стоимость квадратного метра')

resultList = []
for index, item in enumerate(metres):
    if item < 50000:
        a = index
        result = (index+1, item, squares[a])
        resultList.append(result)
resultList.sort(key=lambda x: x[2])
print(resultList)
plt.hlines(50000, 0, 16, color = 'r')
plt.show()

