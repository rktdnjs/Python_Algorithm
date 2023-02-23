# 9086 : 문자열
# https://www.acmicpc.net/problem/9086

import sys

T = int(sys.stdin.readline().strip())

for i in range(0, T):
    string = sys.stdin.readline().strip()
    print(string[:1], string[-1:], sep='')
