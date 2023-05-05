# 18312 : 시각
# https://www.acmicpc.net/problem/18312

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
K = str(K) # 문자로 변환

count = 0
for hour in range(N+1): # N시 59분 59초까지 진행
    if hour < 10:
        hour = '0' + str(hour)
    for minute in range(60): # 59분 까지 진행
        if minute < 10:
            minute = '0' + str(minute)
        for second in range(60): # 59초 까지 진행
            if second < 10:
                second = '0' + str(second)
            if K in str(hour) + str(minute) + str(second):
                count += 1

print(count)