import numpy as np
import matplotlib.pyplot as plt
import time

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
n = 0  # 초기 소수 개수
while n < 100:  # 원하는 소수의 개수 (100개로 설정)
    if is_prime(n):
        primes.append(n)
    n += 1

# 소수의 위치 정보 생성 (역순으로)
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

# 그래프를 한 점씩 추가하고 업데이트
for i in range(len(x)):
    plt.scatter(x[i], y[i], color='blue', s=1)  # s는 점의 크기를 지정합니다.

# 선을 그리기 위한 정보 생성
plt.plot(x[::-1], y[::-1], color='red', linestyle='-')  # 소수의 위치 정보를 역순으로 전달

# 그래프가 완전히 그려지면 종료
plt.show()
