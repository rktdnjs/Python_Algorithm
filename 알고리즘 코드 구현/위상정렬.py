# 위상정렬 시간복잡도 : O(V + E)
# 노드와 간선을 모두 확인한다는 측면에서 위와같이 나옴

from collections import deque

# 노드의 개수 & 간선의 개수
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수 0 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(v + 1)]

# 방향 그래프의 모든 간선 정보 입력
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # 정점 A에서 B로 이동한다는 뜻
    # 진입차수 1 증가
    indegree[b] += 1 # 정점 B의 진입차수(B로 들어오는 간선)

# 위상 정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리

    # 처음 시작할 때는 진입차수 = 0 인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼냄
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수 = 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상정렬 수행 결과 출력
    for i in result:
        print(i, end=" ")

topology_sort()


"""
예시 입출력
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4

1 2 5 3 6 4 7 
"""