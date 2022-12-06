# Имеются данные о продаже компьютеров
# компаний «Ашечка» и «Бэшечка» за последние 6 лет.
# Спрогнозируйте, через сколько лет объёмы
# продаж этих компаний сравняются
#         1 год 2 год 3 год 4 год 5 год 6 год
# Ашечка  1743  1648  1650  1622  1581  1490
# Бэшечка 743   648   711   780   805   846
import matplotlib.pyplot as plt

def FindTrend(comp):
    trend = []
    for i in range(len(comp)-1):
        trend.append(comp[i+1] - comp[i])
    return trend

firstComp = [1743, 1648, 1650, 1622, 1581,1490]
secondComp = [743, 648, 711, 780, 805, 846]

firstTrend = FindTrend(firstComp)
print(firstTrend)

secondTrend = FindTrend(secondComp)
print(secondTrend)

firstMean = 0
for el in firstTrend:
    firstMean += el
firstMean /= len(firstTrend)
print(f'Первая компания растет на {firstMean}')

secondMean = 0
for el in secondTrend:
    secondMean += el
secondMean /= len(secondTrend)
print(f'Вторая компания растет на {secondMean}')

period = 10

for i in range(period):
    firstComp.append(firstComp[-1] + firstMean)

for i in range(period):
    secondComp.append(secondComp[-1] + secondMean)

plt.plot(firstComp)
plt.plot(secondComp)
plt.show()