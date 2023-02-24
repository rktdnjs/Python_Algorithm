# 10988 : 팰린드롬인지 확인하기
# https://www.acmicpc.net/problem/10988

import sys

string = sys.stdin.readline().strip()

if string == string[::-1]:
    print(1)
else:
    print(0)