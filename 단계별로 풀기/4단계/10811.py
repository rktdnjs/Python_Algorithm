# 10811 : 바구니 뒤집기
# https://www.acmicpc.net/problem/10811

import sys

# N = 바구니 개수
# M = 앞으로 입력받을 개수
N, M = map(int, sys.stdin.readline().split())

# 바구니 배열 생성
basket = [i for i in range (1, N + 1)]
# print(basket)

# 이제 슬라이싱 기법을 통해 역순으로 바꾸어준다.
for k in range(0, M):
    # i부터 j번째 바구니의 순서를 역순으로 교체
    i, j = map(int, sys.stdin.readline().split())
    basket[i-1:j] = basket[i-1:j][::-1]
    # i~j번째 바구니에 대한 요소만 바꾼다. 
    # 즉, i~j번째 요소를 슬라이싱하여 역순으로 바꾸고 다시 데이터 업데이트!

for i in basket:
    print(i, end=' ')