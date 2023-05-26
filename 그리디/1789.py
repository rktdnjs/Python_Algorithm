# 1789 : 수들의 합
# https://www.acmicpc.net/problem/1789

import sys

S = int(input())

N = 1

# 1부터 차례대로 계속 더한다.
# 만약 계속 더하다가 S를 초과할 경우 지금까지 더했던 수 중에서 1개를 제외하면 그것이 최선의 선택.
while N * (N + 1) / 2 <= S:
    N += 1

print(N - 1) 