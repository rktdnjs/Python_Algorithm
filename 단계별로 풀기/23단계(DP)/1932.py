# 1932 : 정수 삼각형
# https://www.acmicpc.net/problem/1932

import sys

input = sys.stdin.readline

N = int(input())

numbers = []

for i in range(N):
    numbers.append(list(map(int, input().split())))

# i번째 대각선 수들중에 i-1번째 수랑 더했을 때 큰 수를 i-1번째 리스트에 저장 반복
for i in range(N-1, -1, -1):
    for j in range(i):
        # print(f"i-1 : {i-1}")
        # print(f"j : {j}")
        # print(f"j+1 : {j+1}")
        # print("------")
        numbers[i-1][j] = max(numbers[i-1][j]+numbers[i][j], numbers[i-1][j]+numbers[i][j+1])

# print(numbers)
print(numbers[0][0])