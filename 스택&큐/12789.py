# 12789 : 도키도키 간식드리미
# https://www.acmicpc.net/problem/12789
# 번호순서대로 들어갈 수 있는지 유무를 판단해야함
# count = 1부터 해서 비교하면서 만약 해당 번호를 꺼낼 수 없는 경우 Sad 출력하도록

import sys

input = sys.stdin.readline

N = int(input())
count = 1

# 현재 대기 큐 & 따로 빼내어 대기중인 스택
wait = list(map(int, input().split()))
stack = [] 

# 마지막까지 성공하면 Nice
# 큐를 뒤져보고 그 다음에 스택을 뒤져보기
while True:
    if count >= N + 1:
        print("Nice")
        break

    # 큐 뒤져보기
    # 만약 대기 큐의 맨 앞이 현재 받을 사람 번호표와 같다면
    # 그 사람을 제거하고 count 증가
    # 큐를 뒤졌는데 없으면 그 때 시점의 스택도 뒤져보기
    if len(wait) >= 1:
        if wait[0] == count:
            count += 1
            wait.pop(0)
        else:
            if len(stack) >= 1:
                if stack[-1] == count:
                    count += 1
                    stack.pop(-1)
                    continue
            stack.append(wait.pop(0))

    # 스택 뒤져보기
    else:
        if len(stack) >= 1:
            if stack[-1] == count:
                count += 1
                stack.pop(-1)
            else:
                print("Sad")
                break
        else:
            print("Sad")
            break
    