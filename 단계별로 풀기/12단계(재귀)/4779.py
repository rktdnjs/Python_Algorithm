# 4779 : 칸토어 집합
# https://acmicpc.net/problem/4779
# 파일의 끝에서 입력을 멈춘다 => except EOFError 처리
# 'str' object does not support item assignment : 리스트로 처리해주어야 함
# sys.stdin.readline()은 EOFError를 raise하지 않습니다. input()만 그런 것(!!)

import sys

def divide(start, length):
    if length == 1:
        return
    else: # 예를들어 길이가 27이면 0+9 부터 0+18까지 공백으로 변환(가운데 공백 변환)
        for i in range(start + length//3, start + length//3*2):
            string[i] = ' '
        # 나누어진 파트에 대해서 재귀 호출
        divide(start, length//3)
        divide(start + length//3*2, length//3)
        
while True:
    try:
        N = int(input())
        string = ['-'] * 3**N
        str_len = len(string)
        divide(0, str_len)
        print(''.join(string))
    except EOFError: # EOF
        break