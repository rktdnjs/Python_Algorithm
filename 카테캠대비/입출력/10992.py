# 10992 : 별 찍기 17
# https://www.acmicpc.net/problem/10992

import sys

input = sys.stdin.readline

N = int(input().strip())

for i in range(N):
    print(" "*(N-i-1), end='')

    if i == N-1: # 맨 끝 라인 출력인 경우
        print("*"*(2*i+1))
        break
    
    if i == 0 : # 맨 첫번째 줄 출력할 경우만 특별 처리(^^;;)
        print("*")
    
    if i > 0: # 중간 라인일 경우
        # if i == 0:
        #     continue
        print("*", end='')
        print(" "*(2*(i)-1), end='')
        print("*")


# 1(3) 3(4) 5(5) 7