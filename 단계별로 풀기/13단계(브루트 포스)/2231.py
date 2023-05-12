# 2231 : 분해합
# https://www.acmicpc.net/problem/2231

import sys

N = int(sys.stdin.readline().strip())

count = 0

for i in range(1, N):
    numbers = list(map(int, str(i))) # 생성자를 알아보기 위해 각 숫자를 분리
    number_sum = sum(numbers)
    if N == number_sum + i:
        print(i)
        count += 1
        break

if count == 0:
    print(0)