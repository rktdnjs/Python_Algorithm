# 10828 : 스택
# https://www.acmicpc.net/problem/10828

import sys

N = int(sys.stdin.readline().strip())

stack = [] # 리스트를 이용하여 스택 구현

# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

for i in range(N):
    command = sys.stdin.readline().split() # 명령어를 입력받는다.
    # 입력받고나면, command = [명령어, 숫자] 이런 상황이 된다.
    # 이제 명령어에 따라 다른 처리를 해준다.
    if command[0] == 'push':
        stack.append(command[1])

    elif command[0] == 'pop':
        if len(stack) == 0 : # 스택에 들어있는 정수가 없는 경우
            print(-1)
        else: # 스택에 들어있는 정수가 있을 경우
            print(stack[-1]) # 가장 최근에 들어온 정수를 출력
            stack.pop(-1) # 가장 최근에 들어온 정수를 제거

    elif command[0] == 'size':
        print(len(stack))
    
    elif command[0] == 'empty':
        if len(stack) == 0: # 스택이 비어있을 경우
            print(1)
        else:
            print(0)
    
    elif command[0] == 'top':
        if len(stack) == 0 : # 스택에 들어있는 정수가 없는 경우
            print(-1)
        else: # 스택에 들어있는 정수가 있을 경우
            print(stack[-1]) # 가장 최근에 들어온 정수를 출력
