# 10812 : 바구니 순서 바꾸기
# https://www.acmicpc.net/problem/10812
# 시작 ~ 끝 바구니의 순서를 회전하되, 기준 바구니를 기준으로 회전한다.
# 1 2 3 * 5 6 에서 *이 기준이라고 할 때, 1~5까지 바꾸게 되면
# * 5 1 2 3 6 이 된다.

import sys

N, M = map(int, sys.stdin.readline().split())
# N = 바구니 개수
# M = 회전 시도 횟수

baskets = [i for i in range(1, N + 1)]

# print(baskets)

for i in range(0, M):
    i, j, k = map(int, sys.stdin.readline().split()) # i ~ k ~ j

    tmp = []
    tmp.append(baskets[k-1:j]) # 우선 기준이 되는 바구니~끝 바구니를 땡긴다
    tmp.append(baskets[i-1:k-1]) # 시작~기준이 되는 바구니를 땡긴다
    tmp = sum(tmp, [])
    # sum(iterable, start)는 start에 iterable의 모든 데이터를 더한다.
    # 즉, 여기서 빈 리스트에 각 리스트를 전부 더하게 된다!

    baskets[i-1:j] = tmp # tmp에 저장해놓은, 순서를 회전한 파트를 가져다가 기존의 baskets을 업데이트!

for i in baskets:
    print(i, end=' ')
    