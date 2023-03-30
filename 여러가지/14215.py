# 14215 : 세 막대
# https://www.acmicpc.net/problem/14215
# 23.03.29 기준 9단계 기하 : 직사각형과 삼각형

import sys

input = sys.stdin.readline

length = list(map(int, input().split()))

length.sort() # 오름차순 정렬

# 삼각형은 가장 큰 변의 길이가 나머지 두 변의 합보다 커야한다.
# 3 3 4
# 6 6 10
if(length[0]==length[1]==length[2]):
    print(length[0]*3)
elif(length[2] < length[0] + length[1]):
    print(sum(length))
else:
    print((length[0]+length[1])*2-1)

