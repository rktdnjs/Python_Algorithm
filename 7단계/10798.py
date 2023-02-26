# 10798 : 세로읽기
# https://www.acmicpc.net/problem/10798
# 만약 출력을 잘 해나가다가 다른 단어에 비해 적은 글자수를 가진 단어를 만났다면?
# 공백으로 채워 넣어본다면 어떨까

import sys

words = []

for i in range(0, 5):
    words.append(sys.stdin.readline().strip())

Max = len(max(words, key=len)) 
# max 함수 내부에 key로 len 함수를 전달하여
# Iterable한 자료형에 대해 해당 함수를 적용한 값을 토대로 max값을 찾는다.

for i in range(Max): # 가장 큰 길이의 단어의 길이를 기준으로 각 단어를 쭉 순회
    for j in range(0, 5): # 5개 입력 받았으므로 전체적으로 5번 순회
        if i < len(words[j]): # 만약 특정 단어의 길이가 가장 큰 길이의 단어의 길이보다 작으면 그냥 패스
            print(words[j][i], end='') # 이렇게 돌면서 세로 읽기를 실행