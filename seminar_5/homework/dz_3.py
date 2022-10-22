# Задайте список случайных чисел от 1 до 10. 
# Посчитайте, сколько всего совпадающих элементов 
# есть в списке. Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают
# Список уникальных элементов [1, 4, 2, 3, 6, 7]
import random

numbers = list(random.randint(1,10) for i in range(10))
print(numbers)

counter = {}
 
for i in numbers:
    counter[i] = counter.get(i, 0) + 1
 
doubles = {element: count for element, count in counter.items() if count > 1}
print(doubles)
result = sum(list(doubles.values()))
print(f'сумма всех повторяющихся элементов:', result)
print(f'уникальные числа в списке:', set(numbers))