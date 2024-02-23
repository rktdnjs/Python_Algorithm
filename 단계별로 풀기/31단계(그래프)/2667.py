# 2667 : 단지번호붙이기
# https://www.acmicpc.net/problem/2667
# BFS 사용(DFS로 가능)
# 그래프 BFS & DFS 문제는 dx , dy 활용 

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

# 상하좌우
dx = [1, -1, 0, 0] # 2차원리스트 1번째 인덱스
dy = [0, 0, -1, 1] # 2차원리스트 2번째 인덱스

graph = []
aparts = []
count = 0 # 단지의 집의 수

# sys.stdin.readline은 \n을 포함해 입력을 반환하기에 여기서는 rstrip()을 꼭 사용해야함
for i in range(N):
    graph.append(list(map(int, input().rstrip())))

# BFS 
def bfs(x, y):
    # print(f"시작{x}, {y}")
    queue = deque([])
    queue.append((x, y))
    graph[x][y] = 0
    count = 1
    while queue:
        a, b = queue.popleft()
        for i in range(4): # 해당 점으로부터 4방향 확인
            nx = a + dx[i]
            ny = b + dy[i]

            # 좌표를 확인했는데 그래프를 벗어나게 될 경우
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue # 패스
            
            if graph[nx][ny] == 1: # 아직 방문하지 않았다면
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count # 특정 단지의 탐색이 끝나면 count 반환

    
# 길을 둘러보다가 그래프의 원소가 1이면 BFS로 집 방문
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            count = bfs(i, j)
            aparts.append(count)
            count = 0 # 탐색할때마다 count 초기화

print(len(aparts))
aparts.sort()
for apart in aparts:
    print(apart)

# 입력받은 순서대로 그래프를 보면 아래와 같음
# 0111000
# 0111110
# 0100000
# 0000111
# 1110101
# 0110101
# 0110100