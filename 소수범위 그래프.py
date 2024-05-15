import numpy as np
import matplotlib.pyplot as plt

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# 소수 생성
primes = []
n = 1000  # 원하는 소수의 개수
num = 2  # 시작 소수
while len(primes) < n:
    if is_prime(num):
        primes.append(num)
    num += 1

# 소수의 위치 정보 생성
x = []
y = []
for i, prime in enumerate(primes):
    x.append(prime)
    y.append(i)

# 2D 그래프 생성
plt.figure(figsize=(10, 6))
plt.xlabel('Prime Number')
plt.ylabel('Index')
plt.grid(True)

# 그래프가 천천히 그려지도록 설정
plt.ion()

# 그래프를 한 점씩 추가하고 업데이트
for i in range(len(x)):
    plt.scatter(x[i], y[i], color='blue', s=1)  # s는 점의 크기를 지정합니다.
    plt.title(f'Distribution of Random Primes (Point {i+1}/{len(x)})')
    plt.pause(0.01)  # 각 점을 그리는 간격을 조절합니다.

# 그래프가 완전히 그려지면 종료
plt.ioff()
plt.show()
