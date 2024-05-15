import random
import time
import sys
#플래이어 이름설정
name = input("플래이어의 이름을 정하세요")
name1 = int(name)
#print("안녕하세요" +name1)
#구연 설명
print("어느날 ~~")
#설정
#신분
가문=randint(1,4)
if 1==가문:
        print("당신의 신분은 평민입니다")
if 2==가문:
    print("당신의 신분은 양반입니다")
if 3==가문 :
    print("당신의 신분은 왕족입니다")
if 4==가문:
    print("당신의 신분은 노비입니다")
if 가문==4:
    print("당신은 트롤 가문의 노비입니다")
    a=input("만약 노비 탈출을 원하면 y 아니면 n을 입력해주세요")
    a1=int(a)
    if a1== y:
        mis= 0
        print("노비 탈출 퀘스트")
    if a1==n:
        sys.exit()
if mis==0:
    print("퀘스트: 당신의 이름을 마추면 됩니다")
    name2 = input("당신의 이름은 무엇있가요?")
    name3 = int(name2)
    if name1== name3:
        mis+1
        c=random.randint(1,3)
        가문1=가문 -c
        if 1==가문1:
        print("당신의 신분은 평민입니다")
        print("당신의 직업은 포수입니다")
        print("당신은 활이 필요합니다")
       if 2==가문1:
      print("당신의 신분은 양반입니다")
      if 3==가문1 :
      print("당신의 신분은 왕족입니다")


#상점
print("상점 가는중")
time.sleep(10)
print("환영합니다 여기는 각궁,장궁등이있습니다")
def buy():
    m=1000
    print("당신의 돈은 1000냥입니다 각궁,장궁,배궁,사냥용활이있음니다")
    print("장궁,배궁은 3000냥(1번)")
    print("각궁은 30000냥입니다(2번)")
    print("사냥용활은 500냥입니다(3)")
    print("화살 1000개당 100원입니다(4)")
    print("나가기 (5)")
    u=input("숫자를 고르시요")
    u1= int(u)
    while True:
        if u1 ==1:
          if m >=3000:
             print("구매완료")
            인벤= "장궁"
            m-3000
            brake()
          if m<3000:
             print("구매실패")
    if u1==2:
        if m>=10000:
            print("구매 완료")
            인밴="각궁"
            m-100000
            brake()
        if m<10000:
            print("구매 실패")
    if u1==3:
        if m>= 500:
            print("구매 완료")
            m-500
            brake()
        if500
    if u1==4:
        if m>=100:
            print("구매완료")
            m=100
            brake()
        if m<100:
            print(구매실패
    if u1==5:
        brake()


print("인벤토리 아이템")
print(인벤)
