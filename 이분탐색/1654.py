# 1654 : 랜선 자르기
# https://www.acmicpc.net/problem/1654

import sys
input = sys.stdin.readline

K, N = map(int, input().split())

lan_cables = []

for i in range(K):
    lan_cables.append(int(input()))

max_cable = max(lan_cables)
min_cable = 1
cables_count = 0

# 랜선을 자르면서 N개 이상의 랜선을 구하되, 그 중 길이가 가장 큰 경우를 출력하는 케이스 구하기
# 이분 탐색 사용
while min_cable <= max_cable: # 최소로 설정한 케이블의 길이가 최대와 같아질 때 취소
    mid_cable = (min_cable + max_cable) // 2 # 중간 길이로 잘라서 랜선의 개수를 센다
    cables_count = 0

    for cable in lan_cables:
        cables_count += cable // mid_cable
    
    if cables_count >= N:
        min_cable = mid_cable + 1
    else:
        max_cable = mid_cable - 1

print(max_cable)