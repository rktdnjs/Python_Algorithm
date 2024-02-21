# 1149 : RGB 거리
# https://www.acmicpc.net/problem/1149
# 이웃한 집들끼리 색들이 달라야함
# 흠 그러면 혹시모르기때문에 2번째 작은것에 대해서도 확인해보면 되지 않을까

import sys

input = sys.stdin.readline

N = int(input())

costs = [0] * N

for i in range(N):
    costs[i] = list(map(int, input().split()))

# print(costs)

# 최솟값 계산
# 특정 phase의 최소값을 계산하기 위해서 이전에서 구한 최소값을 이용
# 이전에서 고른 집색깔과 달라야하므로 1 + 2 or 3 / 2 + 1 or 3 / 3 + 1 or 2 계산하여 이어나감
# i번째 i+1번째 라인의 계산값이 2번째 라인에 저장 ... 무한 반복
for i in range(N - 1):
    costs[i+1][0] = min(costs[i][1], costs[i][2]) + costs[i+1][0] # i번째의 2,3번째 중 작은 값과 더해서 i+1번째 라인의 1번째에 업데이트
    costs[i+1][1] = min(costs[i][0], costs[i][2]) + costs[i+1][1] 
    costs[i+1][2] = min(costs[i][0], costs[i][1]) + costs[i+1][2] 

print(min(costs[N-1]))

"""
26 40 83 - 26
49 60 57 - 57
13 89 99 - 13

1 100 100 - 1 
100 1 100 - 1
100 100 1 - 1

30 19 5 - 5
64 77 64 - 64
15 19 97 - 19
4 71 57 - 4
90 86 84 - 84
93 32 91 - 32
"""
