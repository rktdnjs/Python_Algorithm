# 2720 : 세탁소 사장 동혁
# https://www.acmicpc.net/problem/2720
# 23.04.01 기준 8단계 : 일반 수학1

import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    Money = int(input())

    print(Money//25, end=' ')
    Money %= 25
    
    print(Money//10, end=' ')
    Money %= 10

    print(Money//5, end=' ')
    Money %= 5

    print(Money//1)
    Money %= 1