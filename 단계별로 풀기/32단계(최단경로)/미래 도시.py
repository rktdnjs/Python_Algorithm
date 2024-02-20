# 1번 회사 - K - X 회사로 가는 최단 경로 계산
INF = 1000000000

# 전체 회사의 개수 & 경로의 개수
N, M = map(int, input().split())

# 최단 경로 테이블 초기화
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    # A회사에서 B로 갈 수 있음을 나타냄
    # 양방향 이동이 가능하고 이동시 1만큼의 시간이 걸리므로 아래와 같이 저장
    A, B = map(int, input().split()) 
    graph[A][B] = 1
    graph[B][A] = 1

# 1 - K - X 순서로 이동함
X, K = map(int, input().split())

# 거쳐가는 노드 k / 시작 노드 a / 도착 노드 b
for k in range(N + 1):
    for a in range(N + 1):
        for b in range(N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 도달할 수 있다면
if graph[1][K] + graph[K][X] < INF:
    print(graph[1][K] + graph[K][X])
else:
    print(-1)