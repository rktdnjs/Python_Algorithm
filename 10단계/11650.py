# 11650 : 좌표 정렬하기
# https://www.acmicpc.net/problem/11650

import sys

N = int(sys.stdin.readline()) # 입력받을 점의 개수
dots = []

for i in range(0, N):
    x, y = map(int, sys.stdin.readline().split())
    dots.append((x, y))

dots.sort()
for x, y in dots:
    print(x, y)

"""
2차원 평면 위의 점 N개가 주어진다. 
좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력
첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다.
둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다.
위치가 같은 두 점은 없다.
첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.
"""