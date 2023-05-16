# 11478 : 서로 다른 부분 문자열의 개수
# https://www.acmicpc.net/problem/11478

import sys
import time # 시간 측정용

input = sys.stdin.readline

string = input().strip() # 개행 문자 제거
sub_string = [] # 부분 문자열 저장용
str_length = len(string) # 입력받은 문자열의 길이

start_time = time.time() # 시간 측정 시작

for i in range(1, len(string) + 1): # 입력받은 문자열의 길이만큼에 해당하는 인덱스 접근
    start = 0
    end = start + i

    while end < len(string) + 1: # 만약 문자열의 끝 부분을 end가 넘어서면 다음 탐색 시작
        sub_string.append(string[start:end])
        start += 1
        end += 1

print(len(list(set(sub_string))))

# end_time = time.time() # 측정 종료
# print("걸린 시간 : ", end_time - start_time) # 수행 시간 출력
# 걸린 시간 :  0.0009968280792236328