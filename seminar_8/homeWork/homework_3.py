# В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за
# прошлый год. Каждому месяцу соответствует своя строка. Определите самый жаркий и
# самый холодный 7-дневный промежуток этого периода. Выведите его даты
from random import uniform

numbers = [[round(uniform(9, 25), 1) for i in range(31)],
[round(uniform(18, 28), 1) for i in range(30)],
[round(uniform(20, 30), 1) for i in range(31)],
[round(uniform(21, 35), 1) for i in range(31)],
[round(uniform(10, 25), 1) for i in range(30)]]

for rows in numbers:
    print(rows)


for rows in numbers:
    if end < len(rows):
        if sum(rows[start:end]) > max:
            max = sum(rows[start:end])
            start += 1
            end += 1
print(start, end)

