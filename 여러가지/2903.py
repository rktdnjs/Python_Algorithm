# 2903 : 중앙 이동 알고리즘
# https://www.acmicpc.net/problem/2903
# 23.04.04 기준 8단계 : 일반 수학1

import sys

input = sys.stdin.readline

N = int(input())

num = 1 + 2**N

print(num**2)


# 변의 개수
# 1 * 4 = 4
# 2 * 4 = 8
# 4 * 4 = 16
# 8 * 4 = 32
# 
# 점의 개수 - 간격이 2 4 8 16 32... 늘어남
# 1 -> 9 (3^2)
# 2 -> 25 (5^2)
# 3 -> 81 (9^2)
# 4 -> 289 (17^2)
# 5 -> 1089 (33^2)