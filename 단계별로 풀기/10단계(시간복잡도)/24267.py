# 24267 : 알고리즘 수업 - 알고리즘의 수행 시간 6
# https://www.acmicpc.net/problem/24267

import sys

input = sys.stdin.readline

N = int(input())

temp = 0
answer = 0

for i in range(1, N-1):
    temp += i
    answer += temp

print(answer)
print(3) # n^3에 비례하는 시간 복잡도

# n = 7 
# 1 to 5 (i)
# i + 1 to 6 (j)
# j + 1 to 7 (k)
# 1 2 ~ 6 3 ~ 7 5 + 4 + 3 + 2 + 1
# 2 3 ~ 6 4 ~ 7 4 + 3 + 2 + 1
# 3 + 2 + 1
# 2 + 1
# 1 
# 15 + 10 + 6 + 3 + 1 = 35

# n = 6
# 10 + 6 + 3 + 1 = 20