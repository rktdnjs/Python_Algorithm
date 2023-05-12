# 5073 : 삼각형과 세 변
# https://www.acmicpc.net/problem/5073
# 23.04.05 기준 9단계 : 기하 - 직사각형과 삼각형

import sys

input = sys.stdin.readline

while True:
    tri = list(map(int, input().split()))
    if tri == [0, 0, 0]:
        break

    tri.sort() # 정렬을 이용하여 이등변 삼각형 판단
    if tri[2] >= tri[1] + tri[0]:
        print("Invalid")
    elif tri[0] == tri[1] and tri[1] == tri[2] and tri[0] == tri[2]:
        print("Equilateral")
    elif tri[0] == tri[1] or tri[1] == tri[2]:
        print("Isosceles")
    else:
        print("Scalene")