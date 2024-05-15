import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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

# 3D 그래프 생성
fig = plt.figure(figsize=(18, 6))

# 사인 함수
ax1 = fig.add_subplot(131, projection='3d')
ax1.plot_surface(x, y, z_sin, cmap='viridis')
ax1.set_title('Sin Function')

# 코사인 함수
ax2 = fig.add_subplot(132, projection='3d')
ax2.plot_surface(x, y, z_cos, cmap='plasma')
ax2.set_title('Cos Function')

# 탄젠트 함수
ax3 = fig.add_subplot(133, projection='3d')
ax3.plot_surface(x, y, z_tan, cmap='inferno')
ax3.set_title('Tan Function')

plt.show()
