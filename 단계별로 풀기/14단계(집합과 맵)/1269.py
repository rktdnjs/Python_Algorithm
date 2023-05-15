# 1269 : 대칭 차집합
# https://www.acmicpc.net/problem/1269
# 리스트는 차집합을 위한 뺄셈을 지원하지 않는다!
# set 자료형을 이용하면 교집합, 차집합, 합집합을 구할 때 매우 유용하다.
# & 혹은 intersection : 교집합
# | : 합집합
# - : 차집합

import sys
# import time # 시간 측정용

input = sys.stdin.readline

a, b = map(int, input().split())

# start_time = time.time() # 시간 측정 시작

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_B = list(set(A) - set(B))
B_A = list(set(B) - set(A))

print(len(A_B + B_A))

# end_time = time.time() # 측정 종료
# print("걸린 시간 : ", end_time - start_time) # 수행 시간 출력
# 걸린 시간 :  0.3649430274963379