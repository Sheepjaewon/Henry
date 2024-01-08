def solve_linear_equation(a, b):
    if a == 0:
        if b == 0:
            return "해가 무수히 많습니다."
        else:
            return "해가 없습니다."
    else:
        return -b / a

# 사용자로부터 방정식의 계수 a, b 값을 입력받습니다.
a = float(input("a 값을 입력하세요: "))
b = float(input("b 값을 입력하세요: "))

# 1차방정식의 해를 구합니다.
result = solve_linear_equation(a, b)

# 결과 출력
print("해:", result)

