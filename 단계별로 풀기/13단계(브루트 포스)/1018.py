# 1018 : 체스판 다시 칠하기
# https://www.acmicpc.net/problem/1018

import sys

N, M = map(int, sys.stdin.readline().split())
# N : 입력받을 N개의 수
# M : 입력받을 열의 수
# N * M 의 체스판을 입력받고 이중 색칠하는게 최소가 되는 8 * 8 구역의 색칠해야하는 개수를 구한다.

chess = []
count = []

# N번 입력 받는다.
for i in range(N):
    chess.append(sys.stdin.readline().strip())

for n in range(N-7): # 예를 들어 10줄이면 거기서 7을뺀 3까지 진행(8*8 체스판 고려)
    for m in range(M-7):
        W_index = 0 # 시작점이 W로 시작할 경우!
        B_index = 0 # 시작점이 B로 시작할 경우!

        for i in range(n, n+8): # 시작점으로 부터 가로 8줄
            for j in range(m, m+8): # 시작점으로 부터 세로 8줄 확인
                if (i+j) % 2 == 0: # 짝수 홀수 지점을 번갈아 가면서 측정
                    if chess[i][j] != 'W':
                        W_index += 1
                    if chess[i][j] != 'B':
                        B_index += 1
                else:
                    if chess[i][j] != 'B':
                        W_index += 1
                    if chess[i][j] != 'W':
                        B_index += 1
        count.append(min(W_index, B_index))

print(min(count))