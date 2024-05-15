import numpy as np
import matplotlib.pyplot as plt

# 첫 번째 경우: 저항이 10옴이고 전압은 10V
R1 = 10
V1 = 10

# 전류 범위: 1mA ~ 100A
I1 = np.linspace(0.001, 100, 1000)

# 전압 계산
V1_calculated = R1 * I1

# 그래프 그리기
fig, ax = plt.subplots(figsize=(10, 6))
line, = ax.plot(I1, V1 / I1, label='Resistance = 10 ohms, Voltage = 10V')
ax.set_xlabel('Current (A)')
ax.set_ylabel('Resistance (V/I)')
ax.set_title('Ohm\'s Law: Resistance vs Current')
ax.legend()
ax.grid(True)

def onselect(xmin, xmax):
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(V1 / xmax, V1 / xmin)
    plt.draw()

plt.connect('xlim_changed', onselect)

plt.show()
