# 7568 : 덩치(브루트 포스)
# https://www.acmicpc.net/problem/7568

import sys

N = int(sys.stdin.readline().strip())

people = []
count = [] # 덩치 등수 출력용
cnt = 0

for i in range(N):
    people.append(list(map(int, sys.stdin.readline().split())))

for i in range(N): # ..하는 과정을 총 5번 진행
    cnt = 0
    # print(f'{i}번째 트라이') 디버깅용

    for j in range(N): # 입력받은 사람들에 대해서 덩치 비교 수행
        # print(people[i][0], people[j][0], people[i][1], people[j][1]) 디버깅용

        if i == j : # 비교할 대상과 비교 기준 대상이 같은 사람일 경우 그냥 패스
            continue
        elif people[i][0] < people[j][0] and people[i][1] < people[j][1]: # 둘다 크면
            cnt += 1 # 카운트를 1 추가

    count.append(cnt)

for i in count:
    print(i + 1, end=' ')