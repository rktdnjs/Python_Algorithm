# 1260 : DFS & BFS
# https://www.acmicpc.net/problem/1260
# DFS 코드 + BFS 코드 구현 문제
# 정점 번호 작은 것 먼저 방문!!

import sys
from collections import deque

input = sys.stdin.readline

# 정점 개수, 간선 개수, 시작 정점
N, M, V = map(int, input().split())

graph = [[] for i in range(N + 1)] # 간선정보를 담을 그래프

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for sublist in graph: # 작은 정점부터 방문하도록 세팅
    sublist.sort()

# dfs, bfs를 처리할 그래프와 방문 정보 초기화
dfs_graph = graph.copy()
bfs_graph = graph.copy()
dfs_visited = [False] * (N + 1)
bfs_visited = [False] * (N + 1)

# dfs
def dfs(graph, V, visited):
    visited[V] = True # 현재 노드 방문 처리
    print(V, end=" ")
    for vertex in graph[V]: # 현재 방문한 노드와 연결된 노드 중에서
        if not visited[vertex]: # 만약 아직 방문하지 않은 점이 있다면
            dfs(graph, vertex, visited) # 깊이 우선 탐색 진행

# bfs - deque 사용
def bfs(graph, V, visited):
    queue = deque([V]) # 현재 노드를 큐에 삽입
    # 현재 노드 방문 처리
    visited[V] = True
    # 큐가 빌 때까지 반복(시작 노드 기점으로 쫙 진행)
    while queue:
        # 큐에서 하나의 원소를 뽑아냄
        vertex = queue.popleft()
        print(vertex, end=" ")
        # 해당 원소와 연결된 & 아직 방문 X 원소들 큐에다가 쓱싹
        for v in graph[vertex]:
            if not visited[v]: # 아직 방문하지 않았다면
                queue.append(v) # 해당 노드를 큐에 추가
                visited[v] = True # 바로 방문 처리(while 돌리면서 큐에서 빠짐)

dfs(dfs_graph, V, dfs_visited)
print()
bfs(bfs_graph, V, bfs_visited)