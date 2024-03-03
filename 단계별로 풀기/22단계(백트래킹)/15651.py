# 15649 : N과 M (3)
# https://www.acmicpc.net/problem/15651

# 백트래킹은 DFS을 이용하여 풀 수 있음
# 일반적인 DFS와의 차이점은 가지치기를 진행하는 것
# 모든 경우의 수를 탐색하나 조건을 통해 가능성이 없는 경우에는 탐색을 중지하고 이전 노드로 돌아가 다른 경우 탐색
# M이 커질 수록 반복문을 중첩해서 사용해야 하기에 백트래킹을 사용해야함

import sys
# from itertools import permutations

input = sys.stdin.readline

N, M = map(int, input().split())

numbers = []
visited = [False] * (N + 1)

# DFS
# 수열의 개수가 M이 되면 해당 수들을 공백을 기준으로 join하여 출력
# 해당 조건이 만족하지 않을 경우 이미 방문한 케이스에 대해서는 제외
def dfs():
    if len(numbers) == M:
        print(' '.join(map(str, numbers)))
        return
    
    for i in range(1, N + 1):
        # if visited[i]:
        #     continue
        # visited[i] = True
        numbers.append(i)
        dfs()
        numbers.pop() # 재귀를 통해 넣었던 숫자를 다시 pop하고 visited는 False로 바까줌
        # visited[i] = False


# 수열 사전 순 출력
# 중복되는 수열 여러번 출력 X
# N까지 자연수 중 중복 없이 M개를 고른 수열
dfs()

# 4 2
# 1 -> dfs()
# 1 2 이후 numbers.pop
# 1 3 이후 numbers.pop
# 1 4 이후 numbers.pop
# 1 numbers.pop
# 2 ... 반복