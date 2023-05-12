# 2445 : 별 찍기 8
# https://www.acmicpc.net/problem/2445

import sys

input = sys.stdin.readline

N = int(input().strip())

# 상단 파트
for i in range(N):
    print("*"*(i+1), end='')
    print(" "*(2*N - 2*(i+1)) , end='')
    print("*"*(i+1))

# 하단 파트
for i in range(N-1):
    print("*"*(N-i-1), end='')
    print(" "*(2*(i+1)) , end='')
    print("*"*(N-i-1))

"""
1 8 1
2 6 2
3 4 3
4 2 4
5 5
"""