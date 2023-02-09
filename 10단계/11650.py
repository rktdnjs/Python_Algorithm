# 11650 : 좌표 정렬하기
# https://www.acmicpc.net/problem/11650
# 파이썬 내장 함수인 sort를 쓰면 2차원 리스트 또한 오름차순으로 정렬된다.

import sys

N = int(sys.stdin.readline()) # 입력받을 점의 개수
dots = []

for i in range(0, N):
    x, y = map(int, sys.stdin.readline().split())
    dots.append([y, x]) # 리스트 형태로 추가, 이 때 y를 기준으로 정렬할 수 있도록 바꿔서 삽입


dots.sort() # 이렇게 하면 y를 기준으로 점들이 정렬된다.

for y, x in dots: # dots의 점들에 대해서 연산 수행
    print(x, y) # x, y가 거꾸로 되어있었으므로 다시 역으로 출력!

"""
2차원 평면 위의 점 N개가 주어진다. 
좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력
첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다.
둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다.
위치가 같은 두 점은 없다.
첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.
"""

"""
for i in range(0, N):
    x, y = map(int, sys.stdin.readline().split())
    dots.append((x, y))
-> tuple 자료형으로 처리 하는 케이스

print(dots)

dots.sort()
for x, y in dots:
    print(x, y)

"""