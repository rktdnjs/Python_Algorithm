# 1934 : 최소공배수
# https://www.acmicpc.net/problem/1934

import sys

# 큰 수를 작은 수로 나누어 구한 나머지로, 큰 수를 대체한다. 이후 큰 수를 작은 수로 계속 나누는 것을 반복하여 나누어 떨어질 때 까지 반복!
# a를 b로 나누어서 b를 a에 나눈 나머지를 b에 대입시켜서 b가 0이 될 때 까지 반복하면 남는 a 값이 최대 공약수이다.
def GCD(a, b): # 최대공약수 함수
    while b > 0:
        a, b = b, a % b
    return int(a)

# 최소공배수는 a, b의 곱을 a, b의 최대공약수로 나누면 얻을 수 있다.
def LCM(a, b): # 최소공배수 함수
    return int(a * b / GCD(a, b))

input = sys.stdin.readline

T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    print(LCM(A, B))