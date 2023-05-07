# 1260 : DFS와 BFS
# https://www.acmicpc.net/problem/1260

# BFS - 방문했던 노드 목록을 저장할 리스트 & 다음에 방문할 노드의 리스트(큐) 만들기
# 맨 처음에는 시작 노드가 들어간다
# 더 이상 방문할 노드가 없을 때 까지 반복문 진행
# 큐의 맨 앞 노드를 꺼내와서, 해당 노드가 방문 리스트에 없으면 방문리스트에 추가
# 그리고 해당 노드의 자식 노드들을 큐에 추가한다.

# DFS - BFS와 거의 비슷하나, 큐 대신 스택을 사용한다는 점이 다르다.

# 해당 파일은 공부를 좀 더 진행한 이후 다시 수정할 예정

def bfs(graph, start_node):
    visit = list()
    queue = list()

    queue.append(start_node) # 시작 노드를 큐에 추가한다.

    while queue: # queue 리스트에 아무 것도 남지 않을 때 까지 반복한다.
        node = queue.pop(0) # 참고로, pop의 시간 복잡도는O(N)이기 때문에 다른 개선 방법도 생각해보자.
        if node not in visit: # 만약 꺼낸 노드가 방문해보지 않았다면
            visit.append(node) # 해당 노드를 방문 리스트에 추가하고
            queue.extend(graph[node]) # 해당 노드와 연결된 노드들을 큐에 새롭게 추가한다.

    return visit


def dfs(graph, start_node):
    visit = list()
    stack = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])

    return visit


if __name__ == "__main__":
    graph = {
        'A': ['B'],
        'B': ['A', 'C', 'H'],
        'C': ['B', 'D'],
        'D': ['C', 'E', 'G'],
        'E': ['D', 'F'],
        'F': ['E'],
        'G': ['D'],
        'H': ['B', 'I', 'J', 'M'],
        'I': ['H'],
        'J': ['H', 'K'],
        'K': ['J', 'L'],
        'L': ['K'],
        'M': ['H']
    }

    print(bfs(graph, 'A'))
    print(dfs(graph, 'A'))