# 2805 : 나무 자르기
# https://www.acmicpc.net/problem/2805
# 나무의 수 1 ~ 1,000,000
# 나무의 높이 1 ~ 1,000,000,000(엄청 크다!) -> 이진 탐색 고려
# 적어도 M 미터의 나무를 가져가기 위해서 -> 넉넉히 잘랐을 때 이후 적절한 값이 나오지 않으면 정답이므로 기억해야함!!(주의)

import sys

def binary_search(arr, require, start, end):
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        tree_sum = 0
        for tree in arr:
            if tree - mid >= 0:
                tree_sum += tree - mid
        # 잘린 나무 길이들의 합이 요구길이와 동일할 경우
        if tree_sum == require: 
            return mid
        # 잘린 나무 길이들의 합이 요구길이보다 클 경우(나무들을 덜 자르도록...)
        elif tree_sum > require:
            answer = mid # 끝까지 탐색이 끝난경우 최적의 값은 최대한 덜 잘랐을 경우이므로 이 값을 저장
            start = mid + 1
        # 잘린 나무 길이들의 합이 요구길이보다 작을 경우(나무들을 더 자를 수 있도록...)
        else:
            end = mid - 1
    # 끝까지 탐색이 끝난경우 최적의 값은 최대한 덜 잘랐을 경우의 answer를 리턴하는 것
    return answer

input = sys.stdin.readline

N, M = map(int, input().split())

trees = list(map(int, input().split()))

print(binary_search(trees, M, 0, max(trees)))