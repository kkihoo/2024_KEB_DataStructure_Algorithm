import random

n = random.randint(1, 1000)

cnt = 0

while True:
    cnt += 1
    guess = int(input("1~1000 숫자 입력 : "))
    
    if guess < n:
        print("UP !\n")
    elif guess > n:
        print("DOWN !\n")
    elif guess == n:
        print(f"\n!!! Perfect! You got it! in {cnt} chance. !!! ")
        break
    
# 1~100일 경우 log2 수학법칙에 의해 무조건 7회, 1~1000일 경우 무조건 10회 안에 찾기가 가능하다.