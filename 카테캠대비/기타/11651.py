# 11651 : 좌표 정렬하기 2
# https://www.acmicpc.net/problem/11651

import sys

N = int(sys.stdin.readline()) # 입력받을 점의 개수
dots = []

for i in range(0, N):
    x, y = map(int, sys.stdin.readline().split())
    dots.append([y, x]) # 리스트 형태로 추가, 이 때 y를 기준으로 정렬할 수 있도록 바꿔서 삽입


dots.sort() # 이렇게 하면 y를 기준으로 점들이 정렬된다.

for y, x in dots: # dots의 점들에 대해서 연산 수행
    print(x, y) # x, y가 거꾸로 되어있었으므로 다시 역으로 출력!