# 2467 : 용액
# https://www.acmicpc.net/problem/2470

import sys

input = sys.stdin.readline

N = int(input())

# 이미 오름차순으로 정렬된 상태로 입력됨
toxic = list(map(int, input().split()))

# 0 2개 있을 경우 처리
if toxic.count(0) >= 2:
    print(0, 0)

else:
    # 0 2개가 아닌 경우 양 끝 원소에서 줄여가면서 탐색 시작
    start = 0 # 처음 인덱스
    end = N - 1 # 맨 끝 인덱스
    min = abs(toxic[start] + toxic[end]) # 최솟값이 존재할 시 나중에 업데이트

    # 인덱스 저장용
    result_left = 0
    result_right = N - 1

    while True:
        # 합이 0이 아닌 이상 값 업데이트가 진행됨
        result = toxic[start] + toxic[end]

        if result == 0: # 탐색도중 합이 0인 경우
            break

        elif result > 0: # 만약 양수쪽 절댓값이 더 클경우 양수쪽을 땡김
            end -= 1
            if start == end:
                break
            if abs(toxic[start] + toxic[end]) < min:
                result_left = start
                result_right = end
                min = abs(toxic[start] + toxic[end])

        elif result < 0: # 만약 음수쪽 절댓값이 더 클경우 음수쪽을 땡김
            start += 1
            if start == end:
                break
            if abs(toxic[start] + toxic[end]) < min:
                result_left = start
                result_right = end
                min = abs(toxic[start] + toxic[end])
    # print(result_left, result_right)
    print(toxic[result_left], toxic[result_right])

# -99 -2 -1 4 98
# -99 -1 0 1 98
# -100 -2 -1 103