# 13305 : 주유소
# https://www.acmicpc.net/problem/13305

import sys

input = sys.stdin.readline

N = int(input()) # 도시의 수
roads = list(map(int, input().split())) # 도로의 길이
oil_values = list(map(int, input().split())) # 리터당 기름의 값
roads_sum = sum(roads) # 도로길이의 합
min_oil_value = min(oil_values) # 가장 저렴한 기름의 값
res = 0

# 제일 저렴한 기름 값을 가진 도시를 기준으로 구분
# 그 전까지는 그리디하게 처리(포인트)
# 그 이후는 제일 저렴한 기름 값으로 처리하면 끝

if min_oil_value == oil_values[0]:
    res = min_oil_value * roads_sum
else:
    min_oil_index = oil_values.index(min_oil_value) # 가장 저렴한 기름을 가진 도시의 인덱스
    best_oil_roads = roads[min_oil_index:] # 제일 싼 값의 오일로 처리할 부분 슬라이싱
    best_oil_roads_sum = sum(best_oil_roads) # 바로 위 리스트 거리 총합
    best_value = oil_values[0] # 처음 도시의 기름값으로 초기화
    for i in range(min_oil_index): # 가장 저렴한 곳까지 그리디 Go
        if oil_values[i] < best_value:
            best_value = oil_values[i] # 도시의 기름값이 이전보다 저렴하다면 업데이트
        res += best_value * roads[i]
    res += min_oil_value * best_oil_roads_sum

# 결과값 출력
print(res)