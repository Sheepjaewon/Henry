import math

def solve_logarithmic_equation(a, b):
    if a <= 0 or a == 1 or b <= 0:
        return "해가 존재하지 않습니다."

    x = math.pow(a, b)
    return x

# 사용자로부터 a, b 값을 입력받습니다.
a = float(input("a 값을 입력하세요: "))
b = float(input("b 값을 입력하세요: "))

# 로그 방정식의 해를 구합니다.
result = solve_logarithmic_equation(a, b)

# 결과 출력
print("해:", result)
