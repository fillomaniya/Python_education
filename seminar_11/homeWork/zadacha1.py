# Постройте график функции 𝑓(𝑥)=5𝑥^2+10𝑥−30
# По графику определите, при каких значениях
#  x значение функции отрицательно

import numexpr as ne
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

xmin = -20
xmax = 20
dx = 0.01
x = np.arange(xmin, xmax, dx)
print(x)



f = "5*x*x + 10*x - 30"
plt.plot(x, ne.evaluate(f), linewidth=1.5)
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['График функции: f(x) = {}'.format(f)])

plt.hlines(0, -20, 20, color = 'b')

plt.show()