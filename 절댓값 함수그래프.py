import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# x, y 좌표 생성
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
x, y = np.meshgrid(x, y)

# 절댓값 함수의 z 값 계산
z = np.abs(x) + np.abs(y)

# 3D 그래프 생성
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')
ax.set_title('Absolute Value Function')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# x, y, z 축에 대한 눈금 설정
ax.set_xticks(np.linspace(-2, 2, 5))
ax.set_yticks(np.linspace(-2, 2, 5))
ax.set_zticks(np.linspace(0, 4, 5))

plt.show()
