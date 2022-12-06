# Тренер секции по стрельбе получил результаты
# выступления своих спортсменов, где каждое очко означает
# поражённый сектор.
# Помогите ему сымитировать по имеющимся данным
# поражённые мишени.
# Николай: 4, 6, 10, 4, 2, 8, 10, 7, 1, 5
# Александр: 3, 3, 10, 5, 10, 10, 4, 3, 6, 1
# Павел: 2, 2, 1, 1, 3, 7, 9, 9, 2, 8

import matplotlib.pyplot as plt

n = [4, 6, 10, 4, 2, 8, 10, 7, 1, 5]
a = [3, 3, 10, 5, 10, 10, 4, 3, 6, 1]
p = [2, 2, 1, 1, 3, 7, 9, 9, 2, 8]

max_value = 10

n_invert = list(max_value - i for i in n)
a_invert = list(max_value - i for i in a)
p_invert = list(max_value - i for i in p)

ax = plt.subplot(131, polar = True)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_ticks([0, 2, 4, 6, 8, 10])
ax.get_yaxis().set_ticklabels(['10', '8', '6', '4', '2', '0'])
plt.plot(n_invert, 'ro')

ax = plt.subplot(132, projection = 'polar')
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_ticks([0, 2, 4, 6, 8, 10])
ax.get_yaxis().set_ticklabels(['10', '8', '6', '4', '2', '0'])
plt.plot(a_invert, 'go')

ax = plt.subplot(133, projection = 'polar')
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_ticks([0, 2, 4, 6, 8, 10])
ax.get_yaxis().set_ticklabels(['10', '8', '6', '4', '2', '0'])
plt.plot(p_invert, 'yo')

plt.show()