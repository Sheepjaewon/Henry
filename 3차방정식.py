import numpy as np

def solve_cubic_equation(a, b, c, d):
    coefficients = [a, b, c, d]
    roots = np.roots(coefficients)
    return roots

# 사용자로부터 a, b, c, d 값을 입력받습니다.
a = float(input("a 값을 입력하세요: "))
b = float(input("b 값을 입력하세요: "))
c = float(input("c 값을 입력하세요: "))
d = float(input("d 값을 입력하세요: "))

# 3차방정식의 해를 구합니다.
result = solve_cubic_equation(a, b, c, d)

# 결과 출력
print("해:", result)
