# 11723 : 집합
# https://www.acmicpc.net/problem/11723

import sys

input = sys.stdin.readline

s = set()

M = int(input())

for i in range(M):
    command = sys.stdin.readline().split()
    if len(command) == 2:
        command[1] = int(command[1])
    
    if command[0] == "add":
        s.add(command[1])
    elif command[0] == "remove":
        s.discard(command[1]) # remove 말고 discard를 사용하면 원소가 없어도 에러 발생x
    elif command[0] == "check":
        if command[1] in s:
            print("1")
        else:
            print("0")
    elif command[0] == "toggle":
        if command[1] in s:
            s.discard(command[1])
        else:
            s.add(command[1])
    elif command[0] == "all":
        s = {x for x in range(1, 21)}
    elif command[0] == "empty":
        s = set()

# 비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.
# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다. 