# 1463 : 1로 만들기
# https://www.acmicpc.net/problem/1463

import sys

input = sys.stdin.readline

dp = [0] * 10000001

N = int(input())

# dp[1] == 0
# dp[2] == 1이 나오도록

for i in range(2, N+1):
    # 그냥 1을 빼는 경우(일반적인 케이스)
    dp[i] = dp[i-1] + 1
    if i % 2 == 0: # 2로 나누어지는 경우
        dp[i] = min(dp[i], dp[i//2] + 1) # 둘 중 더 최솟값으로 업데이트
    if i % 3 == 0: # 3으로 나누어지는 경우
        dp[i] = min(dp[i], dp[i//3] + 1) # 둘 중 더 최솟값으로 업데이트
    # print(f"{i}번째 dp는 ", dp[i])
    # 해당 과정을 계속해서 진행해나가면, 계속해서 커지는 i에 대해서 최소횟수로 1을 만들 수 있는 과정이 업데이트 되어 횟수가 dp 테이블에 기록된다.

print(dp[N])