# 11557 : Yangjojang of The Year
# https://www.acmicpc.net/problem/11557

import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    lists = []
    N = int(input())
    for i in range(N):
        univ, sool = input().split()
        lists.append([univ, int(sool)])
    lists.sort(key=lambda x : x[1]) # 술 소비량 기준 정렬
    print(lists[-1][0])