# 20920 : 영단어 암기는 괴로워
# https://www.acmicpc.net/problem/20920

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
words = {} # 리스트로 여러번 작업을 시도했더니 시간복잡도 상승, 따라서 딕셔너리 자료형 활용
new_words = []

for i in range(N):
    word = input().rstrip()
    if len(word) >= M:
        if word in words: # 이미 딕셔너리에 값이 있으면 카운트 +1
            words[word] += 1
        else: # 값이 없으면 1로 카운트하고 추가
            words[word] = 1

new_words = list(words.items()) # 딕셔너리를 리스트로 변환

# 차례대로 카운트 값 내림차순 정렬 - 단어 길이 내림차순 정렬 - 사전순 정렬 
new_words = sorted(new_words, key=lambda x : (-x[1], -len(x[0]), x[0]))

for i in range(len(new_words)):
    print(new_words[i][0])