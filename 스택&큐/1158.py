# 1158 : 요세푸스 문제
# https://www.acmicpc.net/problem/1158

# 1 2 3 4 5 6 7
# 3번째 3 제거, 이후 3이 있던 자리를 기준으로 3번째 제거
# 1 2 (3) 4 5 6 7 
# 3기준에서 3번째인 6제거
# 1 2 4 5 7
# 1 2 4 5 6 7 3

import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

# 삭제한 숫자가 들어갈 리스트
delete = []

# K번째 숫자를 제거할 때 사용하기 위한 임시 번호
num = 0

# [1 2 3 4 5 6 ... i]  = arr_list
arr_list = [i for i in range(1, N+1)]

for i in range(N):
    num += K-1 # 예를 들어 K번째 인덱스를 제거하기 위해선 기존에 0번째 인덱스에 위치해 있으므로 K-1을 더해주는 형태로 num을 계산
    if num >= len(arr_list): # 만약 num에 해당하는 숫자를 제거하려고 하는데, 현재 남아있는 원소의 개수보다 작을 경우
        num %= len(arr_list) # arr_list의 길이를 나누어 정상적으로 수행할 수 있도록 변수 조절
    delete.append(str(arr_list[num])) # delete 배열에 제거할 인덱스에 해당하는 숫자를 추가해줌, 이 때 차후 출력의 용이함을 위해 문자열로 저장
    arr_list.pop(num) # num 인덱스에 해당하는 arr_list를 목록에서 제거함

print("<", ", ".join(delete), ">" ,sep="") 
# < 출력 후 구분자는 따로 없이 그냥 쭉 이어서 출력, 이 때 delete 목록의 원소를 , 와 함께 합쳐서 출력해줌 마지막에는 > 출력
# < 출력 후 3, 출력 후 6, .... , 4 출력 후 마지막에 >이 공백없이 이어서 출력됨
# < > 를 제외하고 join으로 , 와함께 숫자 목록이 출력됨