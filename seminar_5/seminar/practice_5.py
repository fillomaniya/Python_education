# Задайте список из 15 случайных чисел.
# Выведите все пары кратных чисел из этого списка.

import random

numbers = list(random.randint(1, 10) for i in range(15))
print(numbers)