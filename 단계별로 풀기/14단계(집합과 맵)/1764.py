# 1764 : 듣보잡
# https://www.acmicpc.net/problem/1764

import sys
import time # 시간 측정용

input = sys.stdin.readline

N, M = map(int, input().split())

start_time = time.time() # 시간 측정 시작

dbj = {} # 듣보잡(예비 후보)
dbj_result = [] # 최종 듣보잡 친구들
dbj_count = 0

for i in range(N):
    name = input().strip()
    dbj[name] = 1

for i in range(M):
    name = input().strip()
    if name in dbj: # 아! 만약 기존 듣보잡 리스트에 있었다면 이 경우 듣보잡이 된다!
        dbj_result.append(name) # 듣보잡에 추가해준다.
        dbj_count += 1
    else : # 사실 여기에 해당하면 더 이상 처리해주지 않아도 됨.
        dbj[name] = 1

print(dbj_count)
dbj_result.sort()

for name in dbj_result:
    print(name)

# 프로그램 소스 코드
# end_time = time.time() # 측정 종료
# print("걸린 시간 : ", end_time - start_time) # 수행 시간 출력
# 걸린 시간 : 0.4821164608001709(측정 결과)