# 11650 : 좌표 정렬하기
# https://www.acmicpc.net/problem/11650
# 파이썬 내장 함수인 sort를 쓰면 2차원 리스트 또한 오름차순으로 정렬된다.

import sys

N = int(sys.stdin.readline()) # 입력받을 점의 개수
dots = []

for i in range(0, N):
    x, y = map(int, sys.stdin.readline().split())
    dots.append([x, y]) # 리스트 형태로 추가

dots.sort()
for x, y in dots:
    print(x, y)


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