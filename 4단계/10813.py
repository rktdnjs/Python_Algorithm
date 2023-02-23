# 10813 : 공 바꾸기
# https://www.acmicpc.net/problem/10813

import sys

# N : 바구니의 개수
# M : 앞으로 공을 바꿀 횟수
N, M = map(int, sys.stdin.readline().split())

baskets = [i+1 for i in range(N)] # N의 개수만큼 i+1을 뚝딱 생성한다.

# print(baskets)

for n in range(0, M): # M번 공을 교체한다.
    # i : i번 바구니의 공과
    # j : j번 바구니의 공을 교체한다.
    i, j = map(int, sys.stdin.readline().split())
    tmp = baskets[i-1] # i번째 바구니의 공을 임시 저장
    baskets[i-1] = baskets[j-1] # j번째 바구니의 공을 i번째로 이동
    baskets[j-1] = tmp
    # print(baskets)

for i in range(0, N):
    print(baskets[i], end=' ')
