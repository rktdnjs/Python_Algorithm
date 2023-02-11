# 23.02.11 아니메컵 2쿨
# A번 - Gorani Command
# https://www.acmicpc.net/contest/problem/939/1
# 고라니의 위치를 구하기 위해서 입력 받은 값의 인덱스를 구해서 값을 출력하는 방식을 이용.
import sys

N, M = map(int , sys.stdin.readline().split()) # 직사각형의 세로 길이 N & 가로 길이 M

x = []
y = []

for i in range(0, N):
    if i == N-1:
        y = list(map(int , sys.stdin.readline().split()))
        x.append(y[0])
        break
    x.append(int(sys.stdin.readline().strip()))
    

print((x.index(min(x))+1), (y.index(min(y))+1) )