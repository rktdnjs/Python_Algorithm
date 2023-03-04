# 1436 : 영화감독 숌
# https://www.acmicpc.net/problem/1436

import sys

N = int(sys.stdin.readline().strip())

count = 0
number = 665

while count != N :
    number += 1
    tmp = number
    tmp = str(tmp)
    if '666' in tmp:
        count += 1

print(number)