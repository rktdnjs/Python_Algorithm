# 4134 : 다음 소수
# https://www.acmicpc.net/problem/4134
# 에라토스테네스의 체 사용
# 소수는 약수가 1과 자기 자신만 존재해야함
# 약수가 있을 경우 약수끼리의 곱으로 수를 표현할 수 있다
# 이를 파악하기 위해서 제곱근 n 까지만 확인해보면 된다

import sys

# 소수를 찾아서 return
def find_sosu(n):

    # 아래 조건에 만족하는 경우 소수가 아닌 것
    while True:
        sqrt = int(n**0.5)
        if n == 1 or n == 0: # 0과 1은 소수가 아니므로 제외 -> 처음 만나는 소수는 2
            return 2
        for j in range(2, sqrt + 1): # 모든 수를 보지 않고, 해당 수의 제곱근까지만 나눠본다.
            if n % j == 0: # 약수가 존재하므로 소수가 아님
                n += 1
                break      # 더이상 검사할 필요가 없으므로 멈춤
        else:
            return n # 만약 나눠지지 않을 경우, 해당 수는 소수임!

input = sys.stdin.readline

N = int(input())

for i in range(N):
    number = int(input())
    print(find_sosu(number))