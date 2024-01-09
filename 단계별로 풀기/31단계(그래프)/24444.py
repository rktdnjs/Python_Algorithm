# 24479 : 알고리즘 수업 - 너비 우선 탐색 1
# https://www.acmicpc.net/problem/24444
# N개의 정점과 M개의 간선
# 정점 R에서 시작하여 DFS로 탐색한 노드의 방문 순서 출력
# 모든 간선의 가중치는 1
# i번째 줄에는 정점 i의 방문 순서를 출력함

import sys
from collections import deque

# 파이썬의 기본 재귀 깊이를 늘리는 방법(Recursion Error 해결법)
# https://fuzzysound.github.io/sys-setrecursionlimit
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

# 정점 간선 시작정점
N, M, R = map(int, input().split())

# 정점 번호 0번은 빈 리스트로 때움
graph = [[] for x in range(N+1)]
sol = [0 for x in range(N+1)]
visited = [False] * (N+1) # 각 노드가 방문된 정보

def bfs(graph, start, visited, sol):
    queue = deque([start]) # BFS를 처리할 큐 구현을 위해 deque 라이브러리 사용
    global count # count가 재귀형태로 실행되므로 전역으로 사용해야 정상적인 답이 나옴
    visited[start] = True
    sol[start] = count
    count += 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                sol[i] = count
                count += 1
        
for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

for sublist in graph:
    sublist.sort()

# 방문하지 못한 노드 개수 0 출력용도
count = 1

# DFS 함수 호출
# 그래프 / 시작 정점 / 방문정보를 넘김
bfs(graph, R, visited, sol)

for i in range(N):
    print(sol[i+1])