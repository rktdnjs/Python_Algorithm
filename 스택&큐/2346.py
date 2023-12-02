# 2346 : 풍선 터뜨리기
# https://www.acmicpc.net/problem/2346

# 1 2 3 4 5
# 3 2 1 -3 -1
# 1->4->5->3->2
# index - value가 연결되어야 함
# enumerate : 인덱스와 원소를 동시에 접근 가능
# 인덱스와 원소로 이루어진 튜플(tuple)을 만들어줌
# deque의 rotate(양수 - 시계방향, 음수 - 반시계방향) & 파이썬의 enumerate 활용하여 문제 풀이
# 해당하는 풍선을 터트린 후 move만큼 덱을 돌려 그 다음 풍선에 index = 0이 위치하도록 함

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
ballons = deque(enumerate(map(int, input().split())))
ballons_arr = []

for i in range(N):
    ballon, move = ballons.popleft()
    ballons_arr.append(ballon + 1)

    if move > 0: # popleft를 함으로써 1칸 반시계방향으로 돌려짐
        ballons.rotate(-(move - 1)) # 따라서 1칸 덜 반시계방향으로 돌림
    else: 
        ballons.rotate(abs(move)) # 이 때는 그냥 시계방향으로 move만큼 회전하면 OK

for i in ballons_arr:
    print(i, end=' ')

