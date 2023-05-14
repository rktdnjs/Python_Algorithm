# 1620 : 나는야 포켓몬 마스터 이다솜
# https://www.acmicpc.net/problem/1620

import sys

input = sys.stdin.readline

# 포켓몬의 개수 / 문제의 개수
N, M = map(int, input().split())

# 내부 처리 시간복잡도를 줄이기 위해 딕셔너리 사용
pocketmons = {}

for i in range(1, N+1):
    pocketmon = input().strip()
    pocketmons[pocketmon] = i
    pocketmons[i] = pocketmon

# print(pocketmons)

for i in range(M):
    question = input().strip()

    if question.isdigit(): # 만약 숫자로 입력이되었다면
        print(pocketmons[int(question)])
    else:
        print(pocketmons[question])
