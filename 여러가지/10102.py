# 10102 : 개표
# https://www.acmicpc.net/problem/10102

import sys

input = sys.stdin.readline

N = int(input())

votes = input().strip()

count_A = 0

for i in votes:
    if 'A' == i:
        count_A +=1

count_B = N - count_A

if count_A > count_B:
    print("A")
elif count_A == count_B:
    print("Tie")
else:
    print("B")