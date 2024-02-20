# 무방향 그래프 내의 사이클 판별시 사용
# 과정은 유니온 파인드와 동일
# 그래프의 모든 간선에 대해 노드의 루트 노드가 같은 것이 있는지 확인
# 만약 같은게 있다면 사이클 발생 O

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

cycle = False # 사이클 발생 여부를 담을 변수

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    # 입력받은 노드들에 대해 사이클이 발생한 경우 종료 시킴
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # 사이클이 발생하지 않았을 경우 union 연산 수행
    else:
        union_parent(parent, a, b)

if cycle:
    print("사이클 발생")
else:
    print("사이클 발생 X")

"""
예시 입출력
3 3
1 2
1 3
2 3
사이클 발생
"""