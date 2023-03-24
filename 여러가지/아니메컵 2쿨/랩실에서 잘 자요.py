# 23.02.11 아니메컵 2쿨
# B번 - 랩실에서 잘 자요(?)
# https://www.acmicpc.net/problem/27446
# 풀다가 일단 냅둠

import sys

# 1 <= N, M <= 100
N, M = map(int , sys.stdin.readline().split())

numList = list(range(1, N+1))

ownpage = list(map(int, sys.stdin.readline().split())) # 바닥에 흩어진 논문
ownpage = list(set(ownpage)) # 중복 제거 후 그 다음에 numList에서 보유한 페이지를 제거한다.

for idx in ownpage:
    numList.remove(idx) # 인쇄해야할 페이지를 알 수 있다.

printList = numList # 출력해야할 페이지를 printList에 저장

distance = 0
ink = 0 

# 프린트해야할 페이지가 1개인 경우 에러가 발생함을 확인 -> 프린트해야할 페이지가 2개 이상인경우 비교하는 것으로 수정

if len(printList) >= 2:
    ink = 0
    for i in range(len(printList) - 1) : # 프린트해야할 페이지가 5개면, 4번 비교 진행
        if i == (len(printList) - 2): # 마지막 비교일 경우
            if printList[i+1] - printList[i] <= 3: # 마지막 비교를 진행할 때 차이가 3이하인 경우 한꺼번에 출력
                distance += printList[i+1] - printList[i]
                ink += 5 + (2*(distance + 1))
            else: # 거리차이가 4이상일 경우
                ink += 5 + (2*(distance + 1)) # 지금까지 계산했던 거리에 따른 프린트 출력 잉크 계산
                ink += 7 # 마지막에 따로 인쇄할 프린트

        elif printList[i+1] - printList[i] <= 3: # 비교를 하다가 거리차이가 3이하일 경우
            distance += printList[i+1] - printList[i]
        
        else: # 거리차이가 4 이상일 경우(한꺼번에 출력하면 손해)
            if distance > 0 : # 기존에 계산했던 거리가 있을 경우
                ink += 5 + (2*(distance + 1)) # 지금까지 계산했던 거리에 따른 프린트 출력 잉크 계산
                distance = 0 # 다시 초기화
            else :
                ink += 7
elif len(printList) == 1:
    ink = 7
else:
    ink = 0

print(ink)

# 출력해야 하는 페이지
# 1 2 6 8 - Test1
# 1 4 7 - Test2

# Test1 

# 연속되어 있을 경우
# 1장 : 7
# 2장 : 9
# 3장 : 11
# 4장 : 13
# 5장 : 15
# 간격이 4이하일 경우까지는 그냥 싹 인쇄하는게 이득
# 그 이상일 경우에는 그냥 따로 인쇄하는게 이득