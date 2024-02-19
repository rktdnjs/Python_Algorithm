# 기본적인 다익스트라 알고리즘

import sys

input = sys.stdin.readline # input 소요 시간 줄이기용
INF = 1000000000 # 거리 테이블을 무한으로 초기화 하기 위함

# 노드의 개수 & 간선의 개수
N, M = map(int, input().split())
# 시작 노드 번호 입력
start = int(input())
# 각 노드와 연결된 노드에 대한 정보를 담는 리스트 생성
graph = [[] for i in range(N + 1)] # 노드의 번호를 인덱스로 바로 리스트에 접근할 수 있게 N + 1
# 방문한 노드가 있는지 체크하는 리스트 생성
visited = [False] * (N + 1)
# 최단 거리 테이블 무한으로 초기화
distance = [INF] * (N + 1)

# 모든 간선 정보 입력
for _ in range(M):
    A, B, C = map(int, input().split())
    # A to B의 비용 = C
    graph[A].append((B, C))

# 방문 X 노드들 중에서 최단 거리가 가장 짧은 노드 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, N + 1): # 순회하면서 가장 짧은 거리의 노드 확인
        if distance[i] < min_value and not visited[i]: # 거리가 가장 짧고 아직 방문 X 라면
            min_value = distance[i]
            index = i
    return index

# 다익스트라 알고리즘 실행
def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True 
    for j in graph[start]: # 시작 노드와 연결된 노드들의 정보들 중
        distance[j[0]] = j[1] # 특정 노드로 가는 길이를 distance에 초기화
        # 예를 들어 1번 노드가 시작일 때 graph[1] = (2, 3), (3, 5) 라면
        # distance[2] = 3 & distance[3] = 5 이렇게 저장 즉 갈 수 있는 노드에 대해 거리를 업데이트 하는 것!
    
    # 시작 노드를 제외한 전체 N - 1개 노드에 대해 최단 경로 길이 탐색
    for i in range(N - 1):
        # 현재 최단 거리가 가장 짧은 노드를 선택하여 방문 처리
        now = get_smallest_node()
        visited[now] = True # 방문 처리!
        # 현재 노드와 연결된 다른 노드들의 거리 확인
        for j in graph[now]:
            cost = distance[now] + j[1] # 현재 해당 노드의 최단 거리 + 다른 노드까지의 거리 확인
            # 만약 위 cost가 현재 까지 업데이트된 거리보다 작을 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 알고리즘 수행
dijkstra(start)

# 출발 노드로부터 다른 노드들까지의 최단 거리 출력
for i in range(1, N + 1):
    # 도달할 수 없는 경우 INF(무한) 출력
    if distance[i] == INF:
        print(f"{i}번 노드로는 갈 수 업읍니다...")
    # 도달할 수 있는 경우 해당 거리 출력
    else:
        print(distance[i])

# 예시 입력
"""
6 11
1
1 2 2 
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2       
"""
"""
5 10
1
1 2 5
1 3 5
1 4 7
2 1 4
2 3 8
2 4 10
3 1 3
3 2 7
3 4 7
4 3 5
"""
# 예시 출력
"""
0
2
3
1
2
4
"""
"""
0
5
5
7
5번 노드로는 갈 수 업읍니다...
"""