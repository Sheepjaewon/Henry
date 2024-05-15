import numpy as np
import matplotlib.pyplot as plt

# x 값 생성
x = np.linspace(-2, 2, 100)

# 지수 함수 그래프
plt.plot(x, np.exp(x), label='exp(x)', color='purple')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Exponential Function')
plt.legend()
plt.show()
