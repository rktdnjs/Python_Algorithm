# 2476 : 주사위 게임
# https://www.acmicpc.net/problem/2476

import sys

input = sys.stdin.readline

N = int(input())

results = []

for i in range(N):
    A, B, C = map(int, input().split())
    if A == B and B == C and A == C:
        results.append(10000 + A*1000)
    elif A == B:
        results.append(1000 + 100 * A)
    elif A == C:
        results.append(1000 + 100 * A)
    elif B == C:
        results.append(1000 + 100 * B)
    else:
        dices = [A, B, C]
        dices.sort()
        results.append(dices[2]*100)

# print(results)
print(max(results))