# 28278 : 스택 2
# https://www.acmicpc.net/problem/28278

import sys

input = sys.stdin.readline

N = int(input())

stack = []

for i in range(N):
    # 입력받은 커맨드에 따라 처리 1, 2, 3, 4, 5
    command = list(map(int, input().split()))

    if command[0] == 1:
        stack.append(command[1])
    elif command[0] == 2:
        if len(stack) >= 1:
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == 3:
        print(len(stack))
    elif command[0] == 4:
        if len(stack) >= 1:
            print(0)
        else:
            print(1)
    elif command[0] == 5:
        if len(stack) >= 1:
            print(stack[-1])
        else:
            print(-1)