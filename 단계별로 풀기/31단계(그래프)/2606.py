# 2606 : 바이러스
# https://www.acmicpc.net/problem/2606
# 1번 컴퓨터가 바이러스에 걸릴 경우 바이러스에 걸리는 컴퓨터의 수
# dfs가 아닌 bfs로도 탐색해서 visited 된 컴퓨터의 수를 세면 풀 수 있음

import sys

input = sys.stdin.readline

N = int(input())
T = int(input()) # 연결된 컴퓨터 쌍의 수

# graph = [[] * (N + 1)] # 연결된 컴퓨터 쌍의 그래프 (주의 : 이렇게 하면 안 됨)
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1) # 각 컴퓨터의 방문 정보
computer = 1

# print(graph)
# print(visited)

for i in range(T):
    a, b = map(int, input().split())
    graph[a].append(b) # a 점에서 b로 갈 수 있음
    graph[b].append(a) # b 점에서 a로도 갈 수 있음

def dfs(graph, computer, visited): # 그래프, 시작 컴퓨터, 방문 정보
    # 현재 컴퓨터 바이러스 감염 처리
    visited[computer] = True
    # 현재 컴퓨터와 연결된 다른 컴퓨터 방문
    for i in graph[computer]:
        # print(f"graph[{computer}] = {i}")
        if not visited[i]:
            # print(f"visit {graph[i]}")
            dfs(graph, i, visited)

dfs(graph, computer, visited)
print(visited.count(True) - 1)
