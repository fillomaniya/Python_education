# Данные торговых точек говорят, что годовая зависимость
# спроса на кофе определяется формулой:
# 𝑦 = 𝑎2𝑥 + 3000
# где:
# y – спрос на кофе
# x – объём стаканчика
# a – количество сахара
# Сколько, примерно, сахара нужно добавлять, чтобы
# кофе объёмом 120 мл покупали 5500 человек,
# а объёмом 205 мл – 6500 человек в год?
# Изначально попробуйте решить задачу с помощью графика

import matplotlib.pyplot as plt

x = [120, 205]

for i in x:
    people = list(i * a * a + 3000 for a in range(0, 10))
    plt.plot(people)

plt.title('Зависимость спроса от количества сахара')
ax = plt.subplot(2, 1, 1)
plot1 = list(5500 for a in range(0, 20))
line, = plt.plot(plot1)
line.set_label('требуемый спрос')

people = list(x[0] * a * a + 3000 for a in range(0, 7))
line, = plt.plot(people)
line.set_label('прогнозируемый спрос')
ax.legend()

ax = plt.subplot(2, 1, 2)
plot1 = list(6500 for a in range(0, 20))
line, = plt.plot(plot1)
line.set_label('требуемый спрос')

people = list(x[1] * a * a + 3000 for a in range(0, 7))
line, = plt.plot(people)
line.set_label('прогнозируемый спрос')
ax.legend()

plt.xlabel('количество сахара')
plt.ylabel('спрос')

plt.show()