# 23.02.11 아니메컵 2쿨
# B번 - 랩실에서 잘 자요(?)
# https://www.acmicpc.net/problem/27446

import sys

ink = 0

N, M = map(int , sys.stdin.readline().split())

numList = list(range(1, N+1)) # 없어진 논문을 찾기 위해서 일단 전체 페이지를 가진 리스트 생성

ownpage = list(map(int, sys.stdin.readline().split())) # 바닥에 흩어진 논문
ownpage = list(set(ownpage)) # 중복 제거 후 numList에서 보유한 페이지를 제거한다.

for idx in ownpage:
    numList.remove(idx) # 인쇄해야할 페이지를 알 수 있다.

# 연속되어 있을 경우
# 1장 : 7
# 2장 : 9
# 3장 : 11
# 4장 : 13
# 5장 : 15
# 간격이 4이하일 경우까지는 그냥 싹 인쇄하는게 이득
# 그 이상일 경우에는 그냥 따로 인쇄하는게 이득