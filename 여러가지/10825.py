# 10825 : 국영수
# https://www.acmicpc.net/problem/10825

# 국어 점수가 감소하는 순서로
# 국어 점수가 같으면 영어 점수가 증가하는 순서로
# 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
# 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로

import sys

input = sys.stdin.readline

N = int(input().strip())
students = []


for i in range(N):
    name, korean, english, math = input().split()
    students.append([name,int(korean), int(english), int(math)])

students.sort(key=lambda x : (-x[1] , x[2] , -x[3] , x[0]))

for i in range(N):
    print(students[i][0])