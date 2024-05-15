import numpy as np
import matplotlib.pyplot as plt

# x, y 좌표 생성
x_min, x_max = -2*np.pi, 2*np.pi
y_min, y_max = -2*np.pi, 2*np.pi
x = np.linspace(x_min, x_max, 100)
y = np.linspace(y_min, y_max, 100)
x, y = np.meshgrid(x, y)

# 각 함수의 z 값 계산
z_sin = np.sin(x + y)
z_cos = np.cos(x - y)
z_tan = np.tan(x * y)

# 2D 그래프 생성
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# 사인 함수
axs[0].imshow(z_sin, cmap='viridis', extent=[x_min, x_max, y_min, y_max])
axs[0].set_title('Sin Function')
axs[0].set_xlabel('x')
axs[0].set_ylabel('y')

# 코사인 함수
axs[1].imshow(z_cos, cmap='plasma', extent=[x_min, x_max, y_min, y_max])
axs[1].set_title('Cos Function')
axs[1].set_xlabel('x')
axs[1].set_ylabel('y')

# 탄젠트 함수
axs[2].imshow(z_tan, cmap='inferno', extent=[x_min, x_max, y_min, y_max])
axs[2].set_title('Tan Function')
axs[2].set_xlabel('x')
axs[2].set_ylabel('y')

plt.show()
