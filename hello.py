from random import *

a = list(range(0, 10))
answer = sample(a, 3)

count = 0

while True:
    strike = 0
    ball = 0
    user = input("3자리 숫자를 입력하세요: ")
    try:
        if len(user) != 3:
            raise ValueError

        f = int(user[0])
        s = int(user[1])
        t = int(user[2])

        if f == s or f == t or s == t:
            raise ValueError

    except ValueError:
        print("다시 입력하세요")
        continue

    print("입력한 숫자는 {}입니다".format(user))

    if f == answer[0]:
        strike += 1
    elif f == answer[1] or f == answer[2]:
        ball += 1

    if s == answer[1]:
        strike += 1
    elif s == answer[0] or s == answer[2]:
        ball += 1

    if t == answer[2]:
        strike += 1
    elif t == answer[0] or t == answer[1]:
        ball += 1

    if strike != 3:
        print("{} 스트라이크, {} 볼 입니다".format(strike, ball))
        count += 1
    elif strike == 3:
        count += 1
        break

print("{} 정답입니다. {}번만에 맞추셨습니다.".format(user, count))

name = input("성함을 입력하세요: ")

with open("score.txt", "a", encoding="utf8") as score:
    score.write("{}\t\t{}\n".format(name, count))

with open("score.txt", "r", encoding="utf8") as score:
    print("\n현재까지 플레이어들의 기록입니다.\n")
    print(score.read())