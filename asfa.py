def fact(n):
    if n<=0:
        print("완료")
        return n
    else:
        fact(n-1)
        print(n-1)

print(fact(10))
