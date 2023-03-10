# 11866 : 요세푸스 문제 0
# https://www.acmicpc.net/problem/11866

# 1 2 3 4 5 6 7
# 3제거 / 1 2 4 5 6 7 / 6(삭제하고 난 후 큐 길이, 다음 연산에 쓰임) | i = 0, x = 2
# 6제거 / 1 2 4 5 7 / 5 | i = 1, x = 4
# 2 / 1 4 5 7 / 5 | i = 2, x = 6 여기서 6 - 5 = 1 1번째 인덱스의 2 출력 
# 7 / 1 4 5 / 4 | i = 3, x = 8
# 5 / 1 4
# 1 / 4

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

people = deque([i for i in range(1, N+1)]) # 리스트를 이용하여 큐 사용

print('<', end='')

for k in range(N):
    for i in range(K - 1): # 해당 for문은 K-1 번째 원소까지 진행한다.
        people.append(people[0]) # 제거하지 않은 요소들은 다시 뒤로 추가
        people.popleft() # 덱의 맨 좌측 요소들을 제거
    print(people.popleft(), end='') # k번째 원소는 제거함!

    if k == N-1:
        print(">")
    else :
        print(", ", end='')