import numpy as np
import matplotlib.pyplot as plt
from turtle import color

plt.figure()
plt.title("Vihmavari")


x1 = np.linspace(-12, 12, 24)
y1 = -(1/18)*x1**2 + 12
plt.plot(x1, y1, color='blue')

x2 = np.linspace(-4, 4, 8)
y2= -(1/18)*x2**2 + 6
plt.plot(x2, y2, color='green')

x3 = np.linspace(-12, -4, 8)
y3= -(1/18)*(8+x3)**2 + 6
plt.plot(x2, y2, color='green')

# Настройки осей
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()