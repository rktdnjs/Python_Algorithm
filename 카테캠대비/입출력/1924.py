# 1924 : 2007년
# https://www.acmicpc.net/problem/1924
# !! 주의 !!
# 파이썬에서 or을 쓸 때 if (i == 1 or 3 or 5 or 7 or 8 or 10 or 12) 요런식으로 쓰게 되면...
# i가 어떤 값인지를 따지는 것이 아닌, i의 타입을 따지는 조건문이다.
# 즉 i(숫자)가 숫자 혹은 숫자 혹은.... 숫자와 같은가 라고 물어보는것과 같다.
# 결론적으로 or은 bool타입 연산자이고, 비교 연산자가 아님에 유의해야한다.

import sys

input = sys.stdin.readline # 이렇게 하면 깔끔하다

x, y = map(int, (input().split()))
days = 0
Day = {'0' : 'SUN', '1' : 'MON', '2' : 'TUE', '3' : 'WED', '4' : 'THU', '5' : 'FRI', '6' : 'SAT'}

for i in range(1, x): # 총 일수 계산

    if (i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12):
        days += 31
    elif (i == 4 or i == 6 or i == 9 or i == 11):
        days += 30
    else :
        days += 28

days += y # 최종적으로 마지막 y일 까지 더해준다.
days = str(days % 7)

print(Day.get(days))
