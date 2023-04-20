# 1850 : 최대공약수
# https://www.acmicpc.net/problem/1850

import sys

input = sys.stdin.readline

a, b = map(int, input().split())
A = 0
B = 0

if a < b: # 큰 친구를 A로 만들어주기
    tmp = b
    b = a
    a = tmp

for i in range(a):
    A += 10**i

for i in range(b):
    B += 10**i

while B != 0:
    tmp = A % B
    A = B
    B = tmp

print(A)