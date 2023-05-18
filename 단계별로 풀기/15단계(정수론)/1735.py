# 1735 : 분수 합
# https://www.acmicpc.net/problem/1735

import sys
import math

input = sys.stdin.readline

# 분자 분모 순
a, b = map(int, input().split())
c, d = map(int, input().split())

# 서로의 분모 분자에 곱할 수
x = b
y = d

# 결과값 분자 분모 저장용
res_up = 0
res_down = 0


a *= y
b *= y
c *= x
d *= x

res_up = a + c
res_down = b # d적어도 상관 없

GCD = math.gcd(res_up, res_down)

print(int(res_up/GCD), int(res_down/GCD))