# 24511 : queuestack
# https://www.acmicpc.net/problem/24511

# 큐에 해당하는 애들만 합치고
# 리스트를 역순으로 뒤집어서 앞에서 부터 M길이 만큼 출력

import sys
from collections import deque

input = sys.stdin.readline

# data_str = deque(enumerate(map(int, input().split()))) deque는 할당 지원 x, 리스트로 풀이
N = int(input())
data_str = list(map(int, input().split()))
data = list(map(int, input().split()))
data_zip = [list(pair) for pair in zip(data_str, data)]
indexes_of_zero = [index for index, value in enumerate(data_str) if value == 0] # 큐에 해당하는 인덱스
res = []
M = int(input())
C = list(map(int, input().split()))
buffer = 0

# 큐에 해당하는 값만 추가, 즉 큐만 따로 다루는 것(스택은 다루지 않아도 상관 x)
# ex) 7 4 2 1 4 -> 4 1 2 4 7
# ex) 4 1(역순) + 2 4 7(이 방식으로)
for i in indexes_of_zero:
    res.append(data[i])

res.reverse()
res += C
res = res[0:M]

for i in range(M):
    print(res[i], end=' ')
