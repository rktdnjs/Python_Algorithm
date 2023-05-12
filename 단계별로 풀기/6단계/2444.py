# 2444 : 별 찍기 7
# https://www.acmicpc.net/problem/2444

import sys

N = int(sys.stdin.readline().strip())

for i in range(1, N+1): # 우선 N번 동안 별 탑 출력
    M = N - i  
    for j in range(0, M): # M-1번 공백출력, N=5일때 처음에는 4번 공백 출력
        print(" ", end='')
    for k in range(0, 2*i-1):
        print("*", end='')
    print()

for i in range(1, N): # 그 다음 N-1 번 동안 별 탑 출력
    M = N - i  
    for j in range(0, i): # M-1번 공백출력, N=5일때 처음에는 4번 공백 출력
        print(" ", end='')
    for k in range(0, 2*M-1):
        print("*", end='')
    print()