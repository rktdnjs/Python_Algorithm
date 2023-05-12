# 2798 : 블랙잭
# https://www.acmicpc.net/problem/2798
# 카드의 개수 + 3장의 합으로 넘지 않아야 하는 수
# 카드의 숫자 입력

import sys
from itertools import combinations # 조합 사용

# 카드의 개수(N)
# 넘지 않아야 하는 수(M)
N, M = map(int, sys.stdin.readline().split())

numbers = list(map(int, sys.stdin.readline().split()))

numbers.sort() # 없어도 상관 없을 듯 하다.

result = 0
tmp = 0

for number in combinations(numbers, 3): #numbers 리스트에서 3개를 아무렇게나 뽑는다(모든 경우의 수 발생)
    tmp = sum(number) # 이 때 number는 for문에서의 결과에 의해 리스트로 반환, 이를 sum을 통해 합을 계산
    if tmp > M:
        continue
    elif result < tmp <= M: # 구한 tmp가 기존 결과보다 크고 M보다 크지 않을 경우에만 업데이트!
        result = tmp

print(result)