# 1966 : 프린터 큐
# https://www.acmicpc.net/problem/1966

import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    target_position = M # M번째 문서가 몇 번째로 인쇄되는지 궁금한 상태
    count = 0 # 문서에서 하나하나 뽑힐 때마다 카운트를 1증가시킨다
    documents = deque(list(map(int, input().split())))

    while documents: # 입력받은 문서들에 대해서 실행
        max_document = max(documents) # 문제 조건에 의해 최대값이 계속 출력될 것
        # 최댓값이 출력되었을 경우에 전체 길이를 1차감할 것
        POP = documents.popleft()
        target_position -= 1 # 덱에서 하나하나 빼낼때마다 우리가 원하는 문서의 위치가 변함

        if POP == max_document: # 만약 이번에 출력된 것이 큐에서 가장 큰 값이라면
            count += 1 # 현재 까지의 출력 횟수 1증가!
            if target_position < 0: # POP하였을 때 target_position이 -1 -> 이 때는 가장 큰 값이 뽑힌 것이므로 끝난것
                print(count)
                break
        
        else: # 만약 이번에 나온 숫자가 큐에서 가장 큰 값이 아니라면
            documents.append(POP)   # 뽑은 숫자를 맨 뒤로 보낸다.
            if target_position < 0: # POP하였을 때 target_position이 -1 -> 즉 우리가 원하는 문서가 맨 뒤로 밀림
                target_position = len(documents) - 1 # 0번째부터 세기 때문에 -1을 해준다.