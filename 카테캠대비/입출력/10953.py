# 10953 : A + B (6)
# https://www.acmicpc.net/problem/10953

import sys

T = int(sys.stdin.readline().strip())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split(',')) # split 내부에 넣은 것을 기준으로 구분지어서 입력 받는다.
    print(A+B)