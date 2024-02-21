# 1904 : 01타일
# https://www.acmicpc.net/problem/1904
# 타일이 00 아니면 1만 있음
# N = 1 / 1
# N = 2 / 11 00
# N = 3 / 111 100 001 
# N = 4 / 1111 1001 0000 1100 0011 
# N = 5 / 11111 00001 00100 10000 11100 11001 10011 00111 8

import sys

input = sys.stdin.readline

N = int(input())

dp = [0] * (N + 1)
dp[1] = 1

# 인덱스 에러 방지
if N >= 2:
    dp[2] = 2
if N >= 3:
    dp[3] = 3


# 규칙 찾아서 걍 그거 적용함(피보나치와 같은 규칙 발견)
# 주의 : 파이썬의 int는 4바이트가 아니다. 따라서 표현하는 수가 커지게 되면 그만큼 메모리 차지
# 이로인해 메모리 초과 에러가 발생하는 것.
# 따라서 이러한 문제를 처리해주어야 한다.
# if N >= 4:
#     for i in range(4, N + 1):
#         dp[i] = dp[i-2] + dp[i-1]

if N >= 4:
    for i in range(4, N + 1):
        dp[i] = dp[i-2] + dp[i-1]
        if dp[i] >= 15746:
            dp[i] = dp[i] % 15746

print(dp[N])

