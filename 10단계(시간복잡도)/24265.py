# 24265 : 알고리즘 수업 - 알고리즘의 수행 시간 4
# https://www.acmicpc.net/problem/24265

import sys

input = sys.stdin.readline

N = int(input())

result = 0

for i in range(N):
    result += i

print(result)
print(2)

# 1 ~ 7
# 1 to 6
# 2 to 7
# 3 to 7
# 6 + 5 + 4 + 3 + 2 + 1