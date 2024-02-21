# 1912 : 연속합
# 연속된 몇개의 수 선택

import sys

input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))

# 1번째 ~... / 2번째 ~ ... / ... / 10번째 선택 연속합 저장
# dp = numbers 이렇게 하면 똑같은 리스트를 참조하는 2개의 레퍼런스가 됨
# dp = [0] * N

# for i in range(N):
#     for j in range(i, N):
#         dp[i] = max(dp[i], sum(numbers[i:j+1]))

for i in range(1, N):
    numbers[i] = max(numbers[i], numbers[i] + numbers[i-1])

print(max(numbers))

# 10 -4 3 1 5 6 -35 12 21 -1 (원본)
# 10 6 3 1 5 6 -35 12 21 -1
# 10 6 9 1 5 6 -35 12 21 -1
# 10 6 9 10 5 6 -35 12 21 -1
# 10 6 9 10 15 6 -35 12 21 -1
# 10 6 9 10 15 21 -35 12 21 -1
# 10 6 9 10 15 21 -14 12 21 -1
# 10 6 9 10 15 21 -14 12 21 -1
# 10 6 9 10 15 21 -14 12 33 -1
# 10 6 9 10 15 21 -14 12 33 32

# 1 -10 10000 100000
# 1 -9  10000 110000

# i번째에서 끝나는 최대 연속합이 i번째 수 자체이거나 그 전까지끝나는 최대 연속합을 더한 것
# 이러한 규칙을 통해 최대인 연속합을 구할 수 있다.