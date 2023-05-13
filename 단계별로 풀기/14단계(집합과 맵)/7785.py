# 7785 : 회사에 있는 사람
# https://www.acmicpc.net/problem/7785

import sys

input = sys.stdin.readline

N = int(input())

# 내부 처리 시간복잡도를 줄이기 위해 딕셔너리 사용
users = {}

for i in range(N):
    user, condition = input().split()
    if condition == "enter":
        users[user] = 'enter'
    elif condition == "leave":
        del users[user]

users = list(users)
users.sort(reverse=True)

for user in users:
    print(user)