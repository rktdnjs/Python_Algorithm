# 25305 : 커트라인
# https://www.acmicpc.net/problem/25305

N, k = map(int, input().split()) # 응시자 수 N 그리고 상을 받는 사람의 수

scores = list(map(int, input().split())) # 점수 목록을 입력 받는다!

scores.sort(reverse=True) # 내림차순 정렬

print(scores[k-1])