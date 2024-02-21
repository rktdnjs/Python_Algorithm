# 1753 : 최단경로
# https://www.acmicpc.net/problem/1753
# 힙 자료구조 -> 시간복잡도 개선

import heapq
import sys

input = sys.stdin.readline
INF = 1000000000

# 정점의 개수 & 간선의 개수
V, E = map(int, input().split())
# 시작 정점의 번호
K = int(input())
# 시작 정점으로부터 다른 정점까지의 거리 테이블 초기화
distance = [INF] * (V + 1)
# 간선 정보를 담을 리스트
graph = [[] for i in range(V + 1)]

# 간선 정보 입력
for _ in range(E): 
    # a에서 b로 가는데 c만큼의 비용 소요
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 다익스트라 알고리즘
def dijkstra(K):
    # 초기 작업 - 우선순위 큐 선언 & 시작 노드의 최단 경로로 큐 삽입 및 시작
    queue = [] # 우선순위 큐(최소힙)
    # 시작 노드로 가기 위한 최단 경로 0으로 세팅 & 큐에 삽입
    heapq.heappush(queue, (0, K)) # (거리, 정점)
    distance[K] = 0 # 시작 정점의 거리 
    while queue:
        # 우선순위 큐 중 가장 최단 거리가 짧은 노드에 대한 정보 꺼냄
        dist, now = heapq.heappop(queue) # (거리, 정점)
        # 현재 정점이 이미 처리된 적이 있다면 무시
        if distance[now] < dist:
            continue
        # 처리된 적이 없다면 인접 노드들을 확인
        else:
            for i in graph[now]: # 현재 정점과 인접한 정점들 중에서
                # 현재 정점을 거쳐 다른 정점으로 가는 거리가 짧다면 업데이트 & 우선순위 큐에 삽입
                cost = dist + i[1] # 현재 정점까지의 거리 + 다른 정점까지의 거리
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(queue, (cost, i[0])) # 갱신된 비용 + 정점
    
dijkstra(K)

for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])