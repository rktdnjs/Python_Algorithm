# 2495 : 가로수
# https://www.acmicpc.net/problem/2485

import sys
import math

input = sys.stdin.readline

N = int(input())
trees = []
distance = []
result = 0

for i in range(N):
    trees.append(int(input()))

# trees.sort()
# print(trees)

for i in range(len(trees) - 1):
    distance.append(trees[i+1]-trees[i])

GCD = distance[0]

# 간격들의 최대 공약수를 구한다
for i in range(1, len(distance)):
    GCD = math.gcd(GCD, distance[i])

# 구한 최대 공약수를 바탕으로 필요한 가로수의 최소 갯수를 구한다
# 총 개수 = 각 간격 // 최대공약수 - 1 한 것을 모두 더함
for dis in distance:
    result += dis // GCD - 1

print(result)