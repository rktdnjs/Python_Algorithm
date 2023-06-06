# 9095 : 1, 2, 3 더하기
# https://www.acmicpc.net/problem/9095

import sys

input = sys.stdin.readline

def ans(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else: # 규칙 : num = 4부터는 이전 3개 식들의 합이 된다.
        return ans(num - 3) + ans(num - 2) + ans(num - 1)

# 규칙을 찾아서 DP로 풀 수 있는 형태인지 확인한다.
# 이후 상향식 혹은 하향식으로 문제를 풀이한다.
# 이 경우 num을 기준으로 호출을 시작하여 맨 하단 까지 내려간다음 다시 재귀를 통해 재활용하는 방식(하향식 : Top-Down)

N = int(input())

for i in range(N):
    num = int(input())
    print(ans(num))