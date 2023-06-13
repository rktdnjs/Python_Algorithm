# 18258 : 큐 2
# https://www.acmicpc.net/problem/18258

import sys
from collections import deque

N = int(sys.stdin.readline().strip())

queue = deque([]) # 덱을 이용하여 큐 구현

for i in range(N):
    command = sys.stdin.readline().split() # 명령어를 입력받는다.
    # 입력받고나면, command = [명령어, 숫자] 이런 상황이 된다.
    # 이제 명령어에 따라 다른 처리를 해준다.
    if command[0] == 'push':
        queue.append(command[1])

    elif command[0] == 'pop':
        if len(queue) == 0 : # 큐에 들어있는 정수가 없는 경우
            print(-1)
        else: # 큐에 들어있는 정수가 있을 경우
            print(queue[0]) # 가장 최근에 들어온 정수를 출력
            queue.popleft() # 가장 최근에 들어온 정수를 제거

    elif command[0] == 'size':
        print(len(queue))
    
    elif command[0] == 'empty':
        if len(queue) == 0: # 큐가 비어있을 경우
            print(1)
        else:
            print(0)
    
    elif command[0] == 'front':
        if len(queue) == 0 : # 큐에 들어있는 정수가 없는 경우
            print(-1)
        else: # 큐에 들어있는 정수가 있을 경우
            print(queue[0]) # 가장 앞에 있는 정수를 출력
    
    elif command[0] == 'back':
        if len(queue) == 0 : # 큐에 들어있는 정수가 없는 경우
            print(-1)
        else: # 큐에 들어있는 정수가 있을 경우
            print(queue[-1]) # 가장 뒤에 있는 정수를 출력