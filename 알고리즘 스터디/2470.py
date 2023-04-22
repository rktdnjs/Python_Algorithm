# 2470 : 두 용액
# https://www.acmicpc.net/problem/2470

import sys

input = sys.stdin.readline

N = int(input())

toxic = list(map(int, input().split()))

toxic.sort() # NlogN 시간복잡도

# 0 2개 있을 경우 처리
if toxic.count(0) >= 2:
    print(0, 0)

# 0 2개가 아닌 경우 양 끝 원소에서 줄여가면서 탐색 시작
min = 1000000000 # 최솟값이 존재할 시 업데이트
start = 0 # 처음 인덱스
end = N-1 # 맨 끝 인덱스

while True: # 둘이 교차할떄 까지 진행
    temp = toxic[start] + toxic[end]
    # start != end
    if temp == 0: # 탐색도중 합이 0이 될 경우
        break

    if temp > 0: # 만약 양수쪽이 더 클 경우, 양수쪽을 줄임
        end = end - 1
        if temp < min: # 만약 지금있던 최솟값인 min보다 작을 경우 값을 업데이트
            min = temp
    elif temp < 0: # 만약 음수쪽 절댓값이 더 클경우, 음수쪽을 줄임
        start = start + 1
        if temp < min: # 만약 지금있던 최솟값인 min보다 작을 경우 값을 업데이트
            min = temp

print(toxic[start], toxic[end])