# 10039 : 평균 점수
# https://www.acmicpc.net/problem/10039

import sys

input = sys.stdin.readline

scores = []

for i in range(5):
    score = int(input())
    if score < 40:
        scores.append(40)
    else:
        scores.append(score)

print(int(sum(scores)/5))