# 어떤 도시에서 다른 모든 도시로 메시지를 보냄
# 받을 수 있는 도시의 개수 & 메시지 수령까지 걸리는 시간 계산
# 한 지점 - 모든 지점 -> 다익스트라
# 시간 복잡도 개선을 위해 우선순위 큐를 이용한 다익스트라 구현

import heapq # 힙 사용을 위함
import sys

input = sys.stdin.readline
INF = 1000000000

# 도시의 개수 & 통로의 개수 & 메시지를 보내고자 하는 도시 
N, M, C = map(int, input().split())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 생성
graph = [[] for i in range(N + 1)]
# 최단 거리 테이블 무한으로 초기화
distance = [INF] * (N + 1)

# 모든 간선 정보 입력
for _ in range(M):
    X, Y, Z = map(int, input().split())
    # X to Y 메시지 전송시간이 Z라는 의미
    graph[X].append((Y, Z))

def dijkstra(start):
    queue = [] # 우선순위 큐(자동으로 최소 힙 상태로 정렬됨, 즉 거리가 짧은 순서대로)
    # 시작 도시로 가기 위한 최단 경로 0으로 설정 & 큐에 삽입
    heapq.heappush(queue, (0, C)) # (거리, 도시)
    distance[C] = 0 # 시작 도시의 거리 0
    while queue: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼냄
        dist, now = heapq.heappop(queue) # 거리, 도시
        # 현재 노드가 이미 처리된 적(꺼낸 노드의 거리가 거리 테이블보다 크다면)이 있다면 무시
        if distance[now] < dist:
            continue
        # 처리된 적이 없다면 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧다면
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0])) # 갱신된 비용 + 노드 큐에 삽입

dijkstra(C)

count_city = 0
time = 0

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, N + 1):
    # 도달할 수 없는 경우 무한 출력
    if distance[i] == INF:
        continue
    # 도달할 수 있는 경우 거리 출력
    elif distance[i] != 0: # 자기 자신으로 오는게 아니면서 도달할 수 있다면
        count_city += 1
        time = max(time, distance[i])

print(count_city, time, end=' ')