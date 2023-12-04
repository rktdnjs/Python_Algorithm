# 26069 : 붙임성 좋은 총총이
# https://www.acmicpc.net/problem/26069

import sys

input = sys.stdin.readline

N = int(input())

rainbow = ["ChongChong"]

for i in range(N):
    humans = list(map(str, input().split()))
    if len(set(humans).intersection(rainbow)) >= 1: # 만약 무지개 춤을 추는 사람이 있을 경우
        rainbow = list(set(rainbow + humans))
    
print(len(rainbow))
        