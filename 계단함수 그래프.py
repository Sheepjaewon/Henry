import numpy as np
import matplotlib.pyplot as plt

# 계단 함수 그래프
x = np.linspace(-2, 2, 100)
y = np.heaviside(x, 0.5)
plt.plot(x, y, label='Heaviside Function', color='orange')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Step Function')
plt.legend()
plt.show()
