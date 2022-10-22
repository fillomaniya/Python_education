# Дан список случайных чисел. Создайте список, 
# в который попадают числа, описывающие 
# возрастающую последовательность. 
# Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
import random

numbers = list(random.randint(1,10) for i in range(10))
print(numbers)

firstList = []
secondList = []
j = 1
 
while j < len(numbers):
  i = j
  N = numbers[:]
  while i < len(N)-1:
    if N[i] < N[i+1]: 
      secondList.append(N[i])
      i += 1
    else:
      N.pop(i+1)
  j+=1
  if len(firstList) < len(secondList):
    firstList = secondList
  secondList=[]
 
if numbers[-1] > firstList[-1]:
  firstList.append(numbers[-1])
  
if numbers[0] < firstList[0]:
  firstList.insert(0, numbers[0])
  
print(firstList)
