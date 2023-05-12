# 10991 : 별 찍기 16
# https://www.acmicpc.net/problem/10991

import sys

input = sys.stdin.readline

N = int(input().strip())

for i in range(N):
    print(" "*(N-i-1), end='')
    print("* "*(i+1))

"""
1

01
101

001
0101
10101

0001
00101
010101
1010101

"""