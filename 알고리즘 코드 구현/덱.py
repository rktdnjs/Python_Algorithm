# 10866 : 덱(Deque)
# https://www.acmicpc.net/problem/10866

import sys

N = int(sys.stdin.readline().strip())

deque = [] # 리스트를 이용하여 덱 구현

# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

for i in range(N):
    command = sys.stdin.readline().split() # 명령어를 입력받는다.
    # 입력받고나면, command = [명령어, 숫자] 이런 상황이 된다.
    # 이제 명령어에 따라 다른 처리를 해준다.

    if command[0] == 'push_front':
        deque.insert(0, command[1]) # insert를 써서 맨 앞에 추가한다.

    elif command[0] == 'push_back':
        deque.append(command[1])
        # deque.insert(-1, command[1]) insert를 쓰는 경우

    elif command[0] == 'pop_front':
        if len(deque) == 0 : # 덱에 들어있는 정수가 없는 경우
            print(-1)
        else: # 덱에 들어있는 정수가 있을 경우
            print(deque[0]) # 덱의 가장 앞의 정수를 출력
            deque.pop(0) # 덱의 가장 앞의 정수를 제거
    
    elif command[0] == 'pop_back':
        if len(deque) == 0 : # 덱에 들어있는 정수가 없는 경우
            print(-1)
        else: # 덱에 들어있는 정수가 있을 경우
            print(deque[-1]) # 덱의 가장 뒤의 정수를 출력
            deque.pop(-1) # 덱의 가장 뒤의 정수를 제거

    elif command[0] == 'size':
        print(len(deque))
    
    elif command[0] == 'empty':
        if len(deque) == 0: # 덱이 비어있을 경우
            print(1)
        else:
            print(0)
    
    elif command[0] == 'front':
        if len(deque) == 0 : # 덱에 들어있는 정수가 없는 경우
            print(-1)
        else: # 덱에 들어있는 정수가 있을 경우
            print(deque[0]) # 가장 앞에 있는 정수를 출력
    
    elif command[0] == 'back':
        if len(deque) == 0 : # 덱에 들어있는 정수가 없는 경우
            print(-1)
        else: # 덱에 들어있는 정수가 있을 경우
            print(deque[-1]) # 가장 뒤에 있는 정수를 출력
