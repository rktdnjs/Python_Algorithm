# 힙 자료구조를 활용한 다익스트라 알고리즘
# 최단 거리가 가장 짧은 노드를 선형적으로 찾는게 아닌 힙을 이용해 빠르게 찾는게 포인트
# 가장 짧은 노드를 힙을 통해 찾기 때문에 기존 다익스트라에서 get_smallest_node 함수 제거
# 시간 복잡도 : O(ElogV)(E : 간선의 개수 / V : 노드의 개수)

import heapq # 힙 사용을 위함
import sys

input = sys.stdin.readline
INF = 1000000000

# 노드의 개수 & 간선의 개수
N, M = map(int, input().split())
# 시작 노드 번호
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 생성
graph = [[] for i in range(N + 1)]
# 최단 거리 테이블 무한으로 초기화
distance = [INF] * (N + 1)

# 모든 간선 정보 입력
for _ in range(M):
    A, B, C = map(int, input().split())
    # A to B 거리가 C라는 의미
    graph[A].append((B, C))

def dijkstra(start):
    queue = [] # 우선순위 큐
    # 시작 노드로 가기 위한 최단 경로 0으로 설정 & 큐에 삽입
    heapq.heappush(queue, (0, start)) # (거리, 노드)
    distance[start] = 0 # 시작 노드의 거리 0
    while queue: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼냄
        dist, now = heapq.heappop(queue) # 거리, 노드
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

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, N + 1):
    # 도달할 수 없는 경우 무한 출력
    if distance[i] == INF:
        print(f"{i}번 노드로는 갈 수 업읍니다..")
    # 도달할 수 있는 경우 거리 출력
    else:
        print(distance[i])