# 2501 : 약수 구하기
# https://www.acmicpc.net/problem/5086
# https://pybasall.tistory.com/171 자주 보는 사이트

import sys

N, K = map(int, sys.stdin.readline().split())

divisor = [] # 약수를 담을 공간

for i in range(1, N+1): # 약수 찾기
    if N % i == 0:
        divisor.append(i) # 약수 추가

# K번째로 작은 약수 출력
if len(divisor) < K: # N의 약수를 찾는데, N의 약수의 개수가 K개 보다 적을 경우
    print(0)
else:
    print(divisor[K-1])