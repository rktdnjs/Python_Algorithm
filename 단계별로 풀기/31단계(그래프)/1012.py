# 1012 : 유기농 배추
# https://www.acmicpc.net/problem/1012

import sys
from collections import deque

# rstrip 주의
input = sys.stdin.readline

# 전체 테스트 케이스 수
T = int(input())

# 상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([])
    queue.append((x, y))
    graph[x][y] = 0
    # print("x, y", x, y)
    while queue:
        a, b = queue.popleft()
        for i in range(4): # 상하좌우 탐색
            my = a + dx[i] # 상하
            mx = b + dy[i] # 좌우

            # 범위를 벗어날 경우
            if mx < 0 or mx >= M or my < 0 or my >= N:
                continue

            if graph[my][mx] == 1: # 배추가 있다면
                # print("my, mx", my, mx)
                queue.append((my, mx))
                graph[my][mx] = 0
    return 1

for i in range(T):
    # 필요한 배추지렁이 수
    jirung = 0

    # 가로길이 / 세로길이 / 배추가 심어진 위치 수
    M, N, K = map(int, input().split())

    graph = [[0 for _ in range(M)] for _ in range(N)]

    for i in range(K):
        y, x = map(int, input().split())
        graph[x][y] = 1 # 배추 위치 기록
    
    # for i in graph:
    #     print(i)

    for i in range(N): # 세로 이동
        for j in range(M): # 가로 이동
            if graph[i][j] == 1:
                jirung += bfs(i, j)
    
    print(jirung)

