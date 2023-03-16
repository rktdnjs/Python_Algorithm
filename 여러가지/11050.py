# 11050 : 이항 계수 1
# https://www.acmicpc.net/problem/11050

import sys

# 팩토리얼 함수는 따로 구현하여 사용.
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

input = sys.stdin.readline

N, K = map(int, input().split())

# 이항계수의 정의를 사용하여 풀이하였다.
# n! / k! (n-k)!
result = factorial(N) // (factorial(K) * factorial(N-K))
print(result)