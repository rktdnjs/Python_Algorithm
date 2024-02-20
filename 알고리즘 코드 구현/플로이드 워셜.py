# 플로이드 워셜 알고리즘 : 모든 지점 to 모든 지점 최단 경로
# 단계마다 '거쳐 가는 노드'를 기준으로 알고리즘 수행
# 모든 노드들 간의 최단 거리 정보를 담아야 하기에 2차원 리스트 활용

INF = 1000000000

# 노드의 개수 & 간선의 개수
N = int(input())
M = int(input())
# 최단 거리 테이블 초기화(2차원 리스트)
graph = [[INF] * (N + 1) for _ in range(N + 1)]
# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b: # 자기 자신 to 자기 자신
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아 해당 값으로 초기화
for _ in range(M):
    # A to B 비용 = C라는 의미
    A, B, C = map(int, input().split())
    graph[A][B] = C

# 점화식에 따라 플로이드 워셜 알고리즘 수행(3중 반복문)
for k in range(1, N + 1): # 거쳐가는 노드
    for a in range(1, N + 1): # 시작 노드
        for b in range(1, N + 1): # 도착 노드
            # a = b or b = c or a = c인 경우는 자기자리로 오는거라 갱신 어차피 안됨
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b]) 

# 수행 결과 출력
for a in range(1, N + 1):
    for b in range(1, N + 1):
        # 도달할 수 없는 경우 무한 출력
        if graph[a][b] == INF:
            print("INF", end = " ")
        # 도달할 수 있는 경우 최단 거리 출력
        else:
            print(graph[a][b], end=" ")
    print() # 줄 띄우기 용


"""
예시 입력
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
"""

"""
예시 출력
0 4 8 6
3 0 7 9
5 9 0 4
7 11 2 0
"""