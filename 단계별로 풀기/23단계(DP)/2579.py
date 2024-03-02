# 2579 : 계단 오르기
# https://www.acmicpc.net/problem/2579
# 계단은 1번에 1개 혹은 2개씩
# 연속된 3개의 계단을 밟으면 안 됨
# 마지막 도착 계단은 반드시 밟아야 함

import sys

input = sys.stdin.readline

N = int(input())

dp = [0] * (N + 1)
stairs = [0]

for i in range(1, N + 1):
    stair_score = int(input())
    stairs.append(stair_score)
    if i == 1:
        dp[i] = stair_score
    elif i == 2:
        # dp[i] = max(stair_score, dp[i-1] + stair_score) # 굳이 모든 경우의 수를 뒤질 필요는 없음. 최대값을 구할 것이기 때문
        dp[i] = dp[1] + stair_score # 걍 이렇게 하면 됨
    else: # i == 3부터
        # i-2 i-1 i 연타는 불가능! 
        # 바로 전칸에서 올라온 케이스(이 때는 3연속 불가능이므로 i-3, i-1 i 순서로 더함) vs 전전칸에서 올라온 케이스
        # 특정 칸의 값은 이전으로부터 2칸을 건너왔거나, 1칸을 건너왔거나 둘 중 하나
        # 후자의 경우에 대해서 3칸을 연속으로 올라오는 것이 안 되므로 i-3 i-1 i 순서로 더하는 것
        dp[i] = max(dp[i-3] + stairs[i-1] + stair_score, dp[i-2] + stair_score)

# 마지막 값중 최대값 출력
print(dp[N])

# 10 20 15 25 10 20
# 1번째 10(No.1)
# 2번째 20 / 10(No.1) + 20
# 3번째 10(No.1) + 15 / 20(No.2_1) + 15 / (10 + 20)(No.2_2) + 15(연속 3계단 불가능, 얘는 제외)
# 4번째  20(No.2_1) + 25 / (10 + 20)(No.2_2) + 25 / (10 + 15)(No.3_1) + 25 / (20 + 15)(No.3_2) + 25 = 60
# dp[1] = 10
# dp[2] = dp[1] + input, input
# (n>=3) dp[n] = dp[n-2] + input or dp[n-1] + input (dp[n-2], dp[n-1]의 모든 케이스들에 대해서 현재 phase의 입력값을 더함)
# 연타로 오는 경우는 어떻게 없애주면 좋을까? => Point

