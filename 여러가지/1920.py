# 1920 : 수 찾기
# https://www.acmicpc.net/problem/1920
# 특정 원소가 어떤 리스트에 들어있는 지 확인하는데에 좀 더 효율적인 방법을 사용해야한다.
# in으로 인한 시간복잡도가 상당하기 때문에, 이분 탐색을 적용한다.
# 집합 정렬 - 시작과 끝 인덱스 설정 - 중간 인덱스 설정 - 찾으려는 값보다 mid가 크거나 작은지에 따라 탐색 진행
# 만약 찾으려는 값이 mid보다 작다면 끝 인덱스를 mid쪽으로 업데이트
# 만약 찾으려는 값이 mid보다 크다면 시작 인덱스를 mid쪽으로 업데이트

import sys

input = sys.stdin.readline

N = int(input())

numbers_list = list(map(int, input().split()))

M = int(input())

find_list = list(map(int, input().split()))
numbers_list.sort() # 정렬 - 탐색을 사용하기 위한 기본 작업, 비교할 리스트를 정렬시켜놓는다.

for number in find_list:
    start = 0
    end = N - 1 # 맨 끝 인덱스 
    find = False

    while start <= end: # end가 start보다 작아지면 이분탐색 종료
        mid = (start + end) // 2 # start와 end의 중간값 = mid
        if number == numbers_list[mid]: # 찾아야하는값이 존재한다면 
            find = True
            print(1)
            break
        elif number > numbers_list[mid]: # 찾아야하는값보다 number가 크다면
            start = mid + 1
        else:
            end = mid - 1
    if find == False:
        print(0)

"""
for i in find_list:
    if i in numbers_list:
        print('1')
    else:
        print('0')
"""