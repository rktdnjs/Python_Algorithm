# 5086 : 배수와 약수
# https://www.acmicpc.net/problem/5086
# https://pybasall.tistory.com/171 자주 보는 사이트

import sys

while True:
    A, B = map(int, sys.stdin.readline().split())
    if A == 0 and B == 0 :
        break
    elif B % A == 0: # B가 A로 나누어 떨어졌다면 A는 B의 약수
        print('factor')
    elif A % B == 0: # A가 B로 나누어 떨어졌다면 A는 B의 배수
        print('multiple')
    else:
        print('neither')