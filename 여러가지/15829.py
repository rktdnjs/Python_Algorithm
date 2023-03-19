# 15829 : Hashing 
# https://www.acmicpc.net/problem/15829
# 입력으로 주어지는 알파벳은 모두 소문자로만 구성되어있다.
# ㅋㅋ mod M을 안해서 50점 나왔음
# M의 값은 1234567891로 하여 처리해주자.

import sys

input = sys.stdin.readline

hash_value = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13,
              'n':14, 'o':15, 'p':16 , 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}

L = int(input())

hash_string = list(input().strip()) # 개행문자 제거

res_value = 0
cnt = 0

for i in hash_string:
    tmp = hash_value.get(i)*(31**cnt)
    cnt += 1
    res_value += tmp

print(res_value % 1234567891)