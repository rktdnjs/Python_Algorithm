# 17103 : 골드바흐 파티션
# https://www.acmicpc.net/problem/17103

# 소수 목록을 구해서 하나하나 선택하여 주어진 숫자에서 뺐을 경우 그 숫자가 소수이면 골드바흐 파티션으로 간주
# 선택한 숫자가 주어진 숫자의 1/2보다 커질 경우 골드바흐 파티션 탐색 종료
# cnt를 하나씩 증가시켜 구하고 결과값 출력
# 주어진 숫자보다 작거나 같은 소수 목록을 구하는 로직
# 소수 목록을 가지고 골드바흐 파티션을 찾아내는 로직

# 다풀어보고 나니 골드바흐 파티션을 찾는과정에서 시간복잡도가 많이 나왔던 것 같다...

import sys

input = sys.stdin.readline

numbers = [1] * 1000001 # 소수 리스트를 미리 구해서 사용 / [1] : 소수임(전부 초기화)
numbers[0] = 0
numbers[1] = 0
sosu = []

for i in range(2, 1000001):
    if numbers[i]: # 만약 이 숫자가 소수라면
        sosu.append(i) # i를 소수 리스트에 추가
        for j in range(i*i, 1000001, i):
            numbers[j] = 0 # i 제곱부터 i의 배수는 전부 소수 x 처리(에라토스테네스의 체 원리)

T = int(input())

for i in range(T):
    cnt = 0
    num = int(input())
    half_num = num * 0.5
    for i in sosu: # 시간복잡도O(n)
        if i > half_num: # 순서 거꾸로 된 것 체크 x용
            break
        else:
            # if num - i in sosu: 시간복잡도O(n)
            #     cnt += 1
            if numbers[i] and numbers[num - i]: # 이렇게 고치니 OK
                cnt += 1
    print(cnt)
