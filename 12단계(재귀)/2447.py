# 2447 : 별 찍기 10
# https://www.acmicpc.net/problem/2447

import sys
# import math

# 기본적으로 3의 거듭제곱에 대한 별을 찍어주기 위해서는 N = 3일 때의 패턴부터 진행한다.
# 그리고 이후 얻어진 패턴들로부터 3번씩 찍어내어서 새로운 패턴을 얻고, 그것이 다음 거듭제곱 패턴이 된다.
# 즉 N = 3일 경우 *** * * *** 패턴이 생기는데 이를 각 라인의 규칙에 따라 3번씩 찍어낸 것이 다음 거듭제곱 패턴!
# 2번째 라인의 규칙에 의해서 중간에 공백이 뻥 하고 뚫린채로 생성된다.
def star(l):
    if l == 3:
        return ['***','* *','***']

    arr = star(l//3) # 계속해서 재귀를 호출하다 보면, 결국 N = 3일 때의 패턴을 리턴하여 활용하게 된다.
    stars = []

    for i in arr: # 1번째 라인
        stars.append(i*3)
        # print(stars)

    for i in arr: # 2번째 라인 - 중간에 공백 생성
        stars.append(i+' '*(l//3)+i)
        # print(stars)

    for i in arr: # 3번째 라인 
        stars.append(i*3)
        # print(stars)

    return stars

N = int(sys.stdin.readline().strip())

print('\n'.join(star(N))) # join함수는 매개변수로 들어온 리스트에 있는 요소를 합쳐서 반환한다.
# 이 코드의 경우, \n 줄바꿈 문자에 의해 줄바꿈 되어 값이 리턴된다.
# join 함수는 -> '구분자(기본값 : 공백)'.join(리스트) 이렇게 사용한다!

"""
재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 
크기 N의 패턴은 N×N 정사각형 모양이다.
크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.
첫째 줄부터 N번째 줄까지 별을 출력한다.
"""