import os
import numpy as np
import matplotlib.pyplot as plt

def f(x,A):
    return -(1+np.cos(12*np.sqrt(x**2-A**2))**2-0.5)/(0.5*(x**2+A**2)+2)

#параметры
A=0
x_values = np.linspace(-5.12, 5.12, 800)

#расчёт координат
y_values = f(x_values, A)
data = [{"x": x, "y": y} for x, y in zip(x_values, y_values)]

#cоздание директории
if not os.path.exists('results'):
    os.makedirs('results')

#сохранение в XML
with open('results/function_values.xml', 'w') as file:
    file.write('<?xml version="1.1" encoding="UTF-8" ?>\n')
    file.write('<data>\n')
    for point in data:
        file.write('\t<row>\n')
        file.write(f'\t\t<x>{point["x"]}</x>\n')
        file.write(f'\t\t<y>{point["y"]}</y>\n')
        file.write('\t</row>\n')
    file.write('</data>')

#построение графика функции
plt.figure(figsize=(16, 9))
plt.plot(x_values, y_values, label='f(x)', color='blue')
plt.title('График функции f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()