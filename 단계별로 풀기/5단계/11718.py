# 11718 : 그대로 출력하기
# https://www.acmicpc.net/problem/11718

import sys

count = 0

while True:
    if count == 100:
        break
    string = sys.stdin.readline().strip()
    print(string)
    count += 1