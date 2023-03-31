# 11005 : 진법 변환 2
# https://www.acmicpc.net/problem/11005
# 23.03.31 기준 8단계 : 일반 수학1

import sys

convert = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N, B = map(int, sys.stdin.readline().split())

count = 0 # 마지막 나눔 처리를 위해 1로 세팅
str = ""

while N != 0: # N, 여기서는 B로나눈 몫이 0이 될 때 까지 진행한다.
    str = str + convert[N % B] # N을 B로 나눈 나머지
    N //= B # N을 B로 나누고 얻은 몫에 대해서 계속 연산 진행

print(str[::-1])
# 예를들어 10을 2진법으로 계산하면 0101(계산시 나오는 나머지 순으로 읽을 경우)
# 그렇기 때문에 이를 거꾸로 읽어주면 문제 x