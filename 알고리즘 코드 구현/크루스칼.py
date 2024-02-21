# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: # a의 부모 노드보다 b의 부모 노드가 크면
        parent[b] = a # b의 부모 노드를 a의 부모 노드로 연결
    else: # a의 부모 노드가 b의 부모 노드보다 크면
        parent[a] = b # a의 부모 노드를 b의 부모 노드로 연결

# 노드의 개수 & 간선(union 연산)의 개수 입력
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

# 부모 테이블상에서 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선을 담을 리스트 & 최종 비용을 담을 변수
edges = []
result = 0

# 모든 간선에 대한 정보 입력받음
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순 정렬을 위해 비용을 튜플의 1번째 원소로 지정
    edges.append((cost, a, b))

# 간선을 비용 순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며 사이클이 발생하지 않을 경우에 집합에 포함
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)

"""
예시 입출력
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
159
"""

"""
3 루트 3 / 3 4
4 루트 3 / 4 7
7 루트 4 / 4 6
6 루트 4 / 6 7
"""