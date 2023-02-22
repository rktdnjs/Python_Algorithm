# 25314 : 코딩은 체육과목 입니다
# https://www.acmicpc.net/problem/25314

import sys

N = int(sys.stdin.readline().strip())

N = N // 4

for i in range(0, N):
    print('long', end=' ')
print('int')