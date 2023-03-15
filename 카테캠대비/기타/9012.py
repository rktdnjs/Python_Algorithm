# 9012 : 괄호
# https://www.acmicpc.net/problem/9012

import sys

input = sys.stdin.readline

T = int(input())

count = 0

for i in range(T):
    count = 0
    VPS = input()
    length = len(VPS)

    for i in range(length):
        if VPS[i] == '(':
            count += 1
        elif VPS[i] == ')':
            count -= 1
            if count < 0 :
                print('NO')
                break
    # 다 돌리고 나서 상황에 따라 YES or NO 출력
    if length-1 == i:
        if count == 0:
            print('YES')
        else : 
            print('NO')

# stack = []

# for i in range(T):
#     stack = [] # 스택 초기화
#     VPS = input()
#     length = len(VPS)

#     for i in range(length):
#         if VPS[i] == '(':
#             stack.append('(')

#         elif VPS[i] == ')':
#             stack.pop('(')