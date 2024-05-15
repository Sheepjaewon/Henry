#재귀함수 사용
def my_factorial(n):
    if(n > 1):
        return n * my_factorial(n - 1)
    else:
        return 1

a = int(input("팩토리얼을 구할 숫자를 입력하세요 : "))
print(my_factorial(a))\

a1=int(inpt("입력하고 싶은 숫자를 입력하세요")
def mytroll(n):
  if n>0:
    print(mytroll)
    return mytroll(n-1)
    
  else:
    print("완료")
print(mytroll(a1))
