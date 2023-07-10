# 13909 : 창문 닫기
# https://www.acmicpc.net/problem/13909
# 특별한 규칙을 발견하여 푸는 문제
# 입력받은 수 N 제곱근의 제곱수개수만큼 출력

import sys
import math

input = sys.stdin.readline

N = int(input()) # N명의 사람과 N명의 창문

cutline = int(math.sqrt(N))

print(cutline)