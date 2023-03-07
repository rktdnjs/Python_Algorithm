# 2446 : 별 찍기 9
# https://www.acmicpc.net/problem/2446

import sys

input = sys.stdin.readline

N = int(input().strip())

for i in range(N): # 상단 파트
    print(" "*i, end='')
    print("*"*(2*N-2*i-1))

for i in range(N-1): # 하단 파트
    print(" "*(N-i-2) , end='')
    print("*"*(2*i+3))