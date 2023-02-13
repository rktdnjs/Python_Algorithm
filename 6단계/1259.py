# 1259 : 팰린드롬 수
# https://www.acmicpc.net/problem/1259
# 앞뒤로 읽어도 똑같은 문자열을 골라내는 로직 작성

import sys

while True:
    N = int(sys.stdin.readline().strip()) # strip은 공백 문자 제거용
    reverseN = int((str(N)[::-1])) # 슬라이싱에서 [시작:끝:규칙] 순으로 들어간다. 규칙 -1이면 거꾸로 한다!
    if N == 0:
        break
    elif N == reverseN:
        print("yes")
    else:
        print("no")

"""
입력은 여러 개의 테스트 케이스로 이루어져 있으며, 각 줄마다 1 이상 99999 이하의 정수가 주어진다.
입력의 마지막 줄에는 0이 주어지며, 이 줄은 문제에 포함되지 않는다.
"""