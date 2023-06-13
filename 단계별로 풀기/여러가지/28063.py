import sys

input = sys.stdin.readline

N = int(input())

x, y = map(int, input().split())

# 가장자리에 있을 경우 2
# 모서리에는 존재하나 가장자리가 아닐경우 3
# 위 경우를 제외한 케이스는 4

if N == 1:
    print(0)
elif x*y == 1 or x*y == N*N or (x==1 and y==N) or (x==N and y==1):
    print(2)
elif x == 1 or x == N or y == 1 or y == N:
    print(3)
else:
    print(4)