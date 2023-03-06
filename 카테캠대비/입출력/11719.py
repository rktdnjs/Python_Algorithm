# 11719 : 그대로 출력하기 2
# https://www.acmicpc.net/problem/11719
# !! input은 EOF를 받을 때 EOF Error를 일으키지만
# sys.stdin.readline은 EOF를 받을 때 빈 문자열을 리턴한다.
# 그렇기 때문에 오류가 발생하지 않고 틀리게 된다는 점에 유의하자.

import sys

while True:
    try:
        print(input())
    except EOFError:
        break