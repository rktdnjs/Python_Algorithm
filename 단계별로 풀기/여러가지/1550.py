# 1550 : 16진수
# https://www.acmicpc.net/problem/1550

import sys

input = sys.stdin.readline

numbers = {'0' : 0, '1': 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, 'A' : 10,
           'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15}

number = list(input().strip())

count = 0
res = 0

for i in range(len(number) - 1, -1, -1):
    # print(i)
    # print(number[i])
    res += 16**count*numbers[number[i]]
    count += 1

print(res)