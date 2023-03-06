# 11721 : 10개씩 끊어 출력하기
# https://www.acmicpc.net/problem/11721

import sys

word = sys.stdin.readline().strip()
count = (len(word)//10 + 1) # 10개 단위씩 끊어서 출력해야 해서 해당 계산식을 사용함


for i in range(count):
    print(word[i*10:i*10+10])

"""
for i in range(0, len(n), 10):
    print(word[i:i+10]) # 띄는 구간을 10으로 설정하여 이렇게도 해결이 가능하다.
"""