# 25192 : 인사성 밝은 곰곰이
# https://www.acmicpc.net/problem/25192

import sys

chat_log = {}

input = sys.stdin.readline
new_count = 0
gom_count = 0

N = int(input())

for i in range(N):
    record = input().strip()

    # 새로운 사용자가 들어오면 채팅 로그 초기화
    if record == "ENTER":
        chat_log = {}
    else: 
        # 유저가 새로운 사용자가 들어온 이후로 채팅 친 목록에 없는 경우
        if record not in chat_log:
            chat_log[record] = 1 # 새롭게 추가함
            gom_count += 1

print(gom_count)