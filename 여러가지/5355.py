# 5355 : 화성 수학
# https://www.acmicpc.net/problem/5355

import sys

input = sys.stdin.readline

N = int(input())

for i in range(N):
    temp = list(input().split())
    temp[0] = float(temp[0]) # 얘만 숫자로 변환
    result = temp[0]
    for i in temp:
        if i == '@':
            result *= 3
            # print('@ 실행')
        elif i == '%':
            result += 5
            # print('% 실행')
        elif i == '#':
            result -= 7
            # print('# 실행')
    print("{:.2f}".format(result))