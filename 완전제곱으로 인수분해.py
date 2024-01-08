def factorize_to_perfect_square(a, b, c):
    # 완전제곱식으로 인수분해하기 위해 a와 b를 찾습니다.
    a_squared = a * a
    b_twice = 2 * a * b
    
    # 변형된 완전제곱식으로 반환합니다.
    result = f"({a}x + {b})^2"
    return result

# 사용자로부터 일차식의 계수 a, b, c 값을 입력받습니다.
a = float(input("a 값을 입력하세요: "))
b = float(input("b 값을 입력하세요: "))
c = float(input("c 값을 입력하세요: "))

# 일차식을 완전제곱식으로 인수분해합니다.
result = factorize_to_perfect_square(a, b, c)

# 결과 출력
print("인수분해 결과:", result)
