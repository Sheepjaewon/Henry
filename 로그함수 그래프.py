import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# x, y 좌표 생성
x = np.linspace(0.001, 100, 100)
y = np.linspace(0.001, 100, 100)
x, y = np.meshgrid(x, y)

# 로그 함수의 z 값 계산
z_log = np.log(x + y)

# 3D 그래프 생성
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z_log, cmap='viridis')
ax.set_title('Log Function')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Log(X + Y)')

plt.show()
