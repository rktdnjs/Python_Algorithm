# 1010 : 다리 놓기
# https://www.acmicpc.net/problem/1010

# 그냥 itertools의 combination의 길이를 구하는 방식으로 했을경우
# 결과 리스트에 대한 길이를 구하는 과정에서도 시간이 많이 소요되어 시간 초과가 발생했음

import sys
from math import factorial

input = sys.stdin.readline

T = int(input())

# 5C2 = 5 4 / 2 1
# 7C4 = 7 6 5 4 / 4 3 2 1
# nCr = n! / (n-r)! r!

def combination_cnt(a, b):
    cnt = factorial(b) / (factorial(b-a) * factorial(a))
    return int(cnt)

for i in range(T):
    A, B = map(int, input().split())
    res = combination_cnt(A, B)
    print(res)