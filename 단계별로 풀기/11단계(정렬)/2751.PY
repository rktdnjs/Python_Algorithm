# 2751 : 수 정렬하기 2
# https://www.acmicpc.net/problem/2751
# 단순히 코드를 짜면 시간 초과 에러가 발생한다.
# 단위가 100만을 넘어가면 시간이 오래 걸리기 때문에, sys.stdin.readline을 사용한다.

import sys

N = int(input())

numbers = []

for i in range(0, N):
    numbers.append(int(sys.stdin.readline()))

numbers = sorted(numbers) # 정렬한 것을 저장 해주어야 함.

for i in numbers:
    print(i)

"""
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
"""