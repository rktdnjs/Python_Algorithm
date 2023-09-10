# 18111 : 마인크래프트
# https://www.acmicpc.net/problem/18111

# 인벤토리에 블럭을 넣는데 2초
# 인벤토리에서 블럭을 꺼내서 배치하는데 1초
# 작업에 걸리는 최소 시간과 땅의 높이 출력
# N * M 크기 & B개의 블럭이 인벤토리에 있음

import sys

input = sys.stdin.readline

N, M, B = map(int, input().split())

blocks = []

for i in range(N):
    blocks += list(map(int, input().split()))

min_height = min(blocks)
max_height = max(blocks)
ans_height = min_height
ans_time = 1000000000
size = N * M

# 가장 낮은 높이의 블록부터 가장 높은 높이의 블록까지 반복하며 확인
for height in range(min_height, max_height + 1):
    blocks_pop, blocks_put = 0, 0
    times = 0

    for j in range(size):
        if blocks[j] > height: # 이 친구들은 캐내야함
            blocks_pop += blocks[j] - height
        else: # 이 경우에는 채워넣어야함
            blocks_put += height - blocks[j]

    if blocks_pop + B >= blocks_put: # 캐낸 블록들과 기존에 있던 블록으로 평탄화를 할 수 있을경우
        times = blocks_pop * 2 + blocks_put
        if times <= ans_time:
            ans_time = times
            ans_height = height

print(ans_time, ans_height)