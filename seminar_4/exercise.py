# Создайте файл random.txt. Запишите в него
# 10 случайных чисел

import random

numbers = []
phrase = 'abcd'
for i in range(10):
    numbers.append(random.randint(1, 10))
print(numbers)

with open('python/seminar_4/random.txt', 'w') as data:
    data.writelines(str(numbers) + '\n')
    data.writelines(phrase)
