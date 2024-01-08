
# 결과 출력
print(f"{num}의 소인수분해 결과:", result)

제곱근방정식
import math

def solve_square_root_equation(c):
    if c < 0:
        return "해가 존재하지 않습니다."

    root1 = math.sqrt(c)
    root2 = -math.sqrt(c)
    return root1, root2

# 사용자로부터 c 값을 입력받습니다.
c = float(input("c 값을 입력하세요: "))

# 제곱근 방정식의 해를 구합니다.
result = solve_square_root_equation(c)

# 결과 출력
print("해:", result)

지수방정식
import math

def solve_exponential_equation(a, b):
    if a <= 0 or a == 1:
        return "해가 존재하지 않습니다."

    x = math.log(b, a)
    return x

# 사용자로부터 a, b 값을 입력받습니다.
a = float(input("a 값을 입력하세요: "))
b = float(input("b 값을 입력하세요: "))

# 지수 방정식의 해를 구합니다.
result = solve_exponential_equation(a, b)

# 결과 출력
print("해:", result)
