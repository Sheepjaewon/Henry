def 재귀함수(n):
    if n==0:
        print("완료")
    else:
        print(n)
        재귀함수(n-1)
print(재귀함수(100))
