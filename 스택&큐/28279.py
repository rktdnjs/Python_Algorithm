# 28279 : 덱 2
# https://www.acmicpc.net/problem/28279

# appendleft, append
# popleft, pop
# clear : 큐의 모든 요소 삭제
# count(x) : 큐에서 x와 같은 값의 개수
# reverse : 큐를 제자리에서 반대로 뒤집음


import sys
from collections import deque

input = sys.stdin.readline
dequeue = deque([])
N = int(input())

for i in range(N):
    command = list(map(int, input().split()))
    length = len(dequeue)

    # 덱의 앞에 정수 추가
    if command[0] == 1:
        dequeue.appendleft(command[1])
    # 덱의 뒤에 정수 추가    
    if command[0] == 2:
        dequeue.append(command[1])
    # 덱의 앞에서 정수를 빼고 출력, 없으면 -1
    if command[0] == 3:
        if length >= 1:
            print(dequeue.popleft())
        else:
            print(-1)
    # 덱의 뒤에서 정수를 빼고 출력, 없으면 -1
    if command[0] == 4:
        if length >= 1:
            print(dequeue.pop())
        else:
            print(-1)
    # 덱의 정수 개수 출력
    if command[0] == 5:
        print(length)
    # 덱이 비어있으면 1, 아니면 0
    if command[0] == 6:
        if length >= 1:
            print(0)
        else:
            print(1)
    # 덱에 정수가 있다면 맨 앞 출력, 없으면 -1
    if command[0] == 7:
        if length >= 1:
            print(dequeue[0])
        else:
            print(-1)
    # 덱에 정수가 있다면 맨 뒤 출력, 없으면 -1
    if command[0] == 8:
        if length >= 1:
            print(dequeue[-1])
        else:
            print(-1)