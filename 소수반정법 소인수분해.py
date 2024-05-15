from numba import jit

@jit(nopython=True)
def factorize(n):
  """
  주어진 숫자를 소인수 분해합니다.
  """
  factors = []
  divisor = 2
  while divisor * divisor <= n:
    while n % divisor == 0:
      factors.append(divisor)
      n //= divisor
    divisor += 1
  if n > 1:
    factors.append(n)
  return factors

# 예시
n = 1247129158724311332487124681743043798132475647891243712481740957891
factors = factorize(n)
print(f"소인수 분해 결과: {factors}")
