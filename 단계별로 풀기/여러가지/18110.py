# 18110 : solved.ac
# https://www.acmicpc.net/problem/18110

# 위 & 아래 15% 반올림한 숫자만큼의 사람들을 평균 계산에서 제외
# 최종계산된 평균도 반올림

import sys 

# 파이썬의 오사오입 문제가 발생하지 않는 반올림 함수
def roundNumber(num):
    return round(num + 10**(-len(str(num)) - 1))

input = sys.stdin.readline

N = int(input())

# 의견이 없으면 난이도 0
if N == 0:
    print(0)
    exit()

scores = []

for i in range(N):
    scores.append(int(input()))

scores.sort()

# 전체 사람의 15% 계산
people = roundNumber(len(scores) * 0.15)

# 예를들어 people = 1였으면 [0 ,v , v , v, -1] 이렇게 슬라이싱
if people == 0: 
    scores = scores # 변동 없음
else: scores = scores[people:-people]

# 평균 구해서 반올림
print(roundNumber(sum(scores)/len(scores)))