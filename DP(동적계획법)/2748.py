# 2748 : 피보나치 수 2
# https://www.acmicpc.net/problem/2748

import sys

input = sys.stdin.readline

N = int(input())

dp = [0] * (N + 2)

for i in range(N):
    if i == 0:
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
    else:
        dp[i+2] = dp[i] + dp[i+1]

print(dp[N])