# 11404 : 플로이드
# https://www.acmicpc.net/problem/11404

import sys

input = sys.stdin.readline

INF = 1000000000

# 도시의 개수
N = int(input())
# 버스의 개수(간선)
M = int(input())
# 버스의 정보를 담을 리스트(최단거리 테이블)
graph = [[INF] * (N + 1) for _ in range(N + 1)]

# 최단거리 테이블 중 자기자신으로 돌아가는 비용만 0으로 초기화(2중 반복문)
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            graph[i][j] = 0

# 버스의 정보
for i in range(M):
    # 한 지점에서 한 지점까지의 거리 입력
    a, b, c = map(int, input().split())
    if graph[a][b] <= c: # 만약 기존에 더 적은 비용의 노선이 있을 경우
        continue
    else:
        graph[a][b] = c # a에서 b로가는데 c만큼의 비용

# 플로이드 워셜(3중 반복문)
for k in range(1, N + 1): # 거쳐가는 포인트
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

# 결과 출력
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()
