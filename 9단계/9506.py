# 9506 : 약수들의 합
# https://www.acmicpc.net/problem/9506

import sys

while True:
    divisor = [] # 약수를 담을 공간

    N = int(sys.stdin.readline())

    if N == -1:
        break

    for i in range(1, N): # 약수 찾기
        if N % i == 0:
            divisor.append(i) # 약수 추가

    # 만약 N이 완전수일 경우
    if sum(divisor) == N : # 약수의 합 == N일 때!
        # print(f"N = ")
        print(N, end=' ')
        print('=', end=' ')

        for i in divisor: # 약수들에 대해서
            if divisor.index(i) == (len(divisor) - 1):
                print(i)
                break
            print(i, end=' ')
            print('+', end=' ')
    

    # N이 완전수가 아닐 경우
    else :
        print(f"{N} is NOT perfect.")
