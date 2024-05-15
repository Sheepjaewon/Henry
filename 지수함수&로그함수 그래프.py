import numpy as np
import matplotlib.pyplot as plt

# 지수와 로그를 결합한 함수 그래프
x = np.linspace(0.001, 10, 100)
y = x * np.log(x)
plt.plot(x, y, label='y = x * log(x)', color='green')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Function Combining Exponential and Logarithm')
plt.legend()
plt.show()
