from ursina import *
from random import choice, random

# Ursina 앱 초기화
app = Ursina()

# 3D 그래픽을 위한 클래스
class FloatingShape(Entity):
    def __init__(self):
        super().__init__(
            model=choice(['cube', 'sphere', 'plane']),  # 무작위로 모델 선택
            color=color.random_color(),  # 무작위 색상 선택
            position=(random()*20-10, random()*10, random()*20-10),  # 무작위 위치 선택
            scale=random() * 3  # 무작위 크기 선택
        )

# 떠다니는 모양들을 담을 리스트
floating_shapes = []

# 무작위로 생성된 떠다니는 모양들을 생성
for _ in range(20):
    shape = FloatingShape()
    floating_shapes.append(shape)

# 카메라 설정
camera.position = (0, 10, -20)
camera.rotation_x = 45

# 엔진 실행
app.run()
