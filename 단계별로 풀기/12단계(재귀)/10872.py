# 10872 : 팩토리얼
# https://www.acmicpc.net/problem/10872

import sys

def factorial(N): # 팩토리얼 재귀 함수 정의
    if N == 0:
        return 1
    if N == 1:
        return 1 # 만약 N이 1에 도달하였다면 1을 반환
    return N * factorial(N - 1) # N과 factorial(N - 1)을 곱함

N = int(sys.stdin.readline().strip()) # strip -> 개행 문자 제거용

print(factorial(N))