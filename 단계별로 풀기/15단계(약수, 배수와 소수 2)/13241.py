# 13241 : 최소공배수
# https://www.acmicpc.net/problem/13241

import sys
import math

input = sys.stdin.readline

A, B = map(int, input().split())

print(math.lcm(A, B))