# 2745 : 진법 변환
# https://www.acmicpc.net/problem/2745
# 23.03.31 기준 8단계 : 일반 수학1

import sys
# import math # 거듭제곱 계산을 위한 라이브러리 (안 씀)

convert = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N, B = sys.stdin.readline().split()

B = int(B) # 정수형으로 변경
N = N[::-1]

result = 0

# 문자를 하나씩 떼와서 convert에 해당하는 인덱스를 가져옴, 그리고 거기에 대해서 진법 변환 실행
for i in range(len(N)):
    result += (convert.index(N[i]))*(B**i)

print(result)