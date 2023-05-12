# 10810 : 공 넣기
# https://www.acmicpc.net/problem/10810

import sys

# N : 바구니의 개수
# M : 앞으로 공을 넣을 횟수
N, M = map(int, sys.stdin.readline().split())

baskets = [0 for i in range(N)] # 0에 대해서 N의 개수만큼 원소 0을 채워넣는다.

# print(baskets)

for n in range(0, M): # M번 공을 넣는다.
    # i : i번 바구니부터
    # j : j번 바구니까지
    # k : k번에 해당하는 공을 넣는다.
    i, j, k = map(int, sys.stdin.readline().split())
    baskets[i-1:j] = [k for i in range(0, j-i+1)] # i번 ~ j번 바구니에 k로 바꿔치기!
    # print(baskets[i:j+1]) 디버깅 용
    # print(baskets)
    # print([k for i in range(0, j-i+1)])

for i in range(0, N):
    print(baskets[i], end=' ')
