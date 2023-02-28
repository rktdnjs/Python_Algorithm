# 10870 : 피보나치 수 5
# https://www.acmicpc.net/problem/10870

import sys

def fibonachi(N):
    if N == 0:
        return 0
    if N == 1:
        return 1 # 만약 N이 1에 도달하였다면 1을 반환
    return fibonachi(N-1) + fibonachi(N-2)

N = int(sys.stdin.readline().strip())

print(fibonachi(N))

"""
첫째 줄에 n번째 피보나치 수를 출력한다.
"""