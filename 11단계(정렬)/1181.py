# 1181 : 단어 정렬
# https://www.acmicpc.net/problem/1181
# 기본적으로 sort() 함수는 오름차순으로 정렬해주는 함수이다.
# sort(reverse=Ture) 혹은 reverse()를 사용하여 내림차순으로도 구현이 가능하다.
# 참고로 sort와 sorted가 있는데, sorted는 원본을 변형시키지 않는다.
# sort와 sorted 모두 key, reverse 매개변수를 갖고 있다!
# 1.reverse에는 bool값을 넣으며 True로 설정하면 내림차순으로 정렬한다.
# 2.key는 정렬을 목적으로 하는 함수를 값으로 넣으며, 람다(lambda)를 이용할 수 있다!
# 이 때 key 값을 기준으로 정렬되고 기본값은 오름차순이다.
# 중복 제거는 set 함수의 성질을 이용하여 같은 요소를 제거해준다.
import sys

N = int(sys.stdin.readline()) # 입력받을 단어의 개수
words = []

for i in range(0, N):
    words.append(sys.stdin.readline().strip()) # strip()을 통해 공백 문자를 제거해준다.

words = list(set(words)) # 리스트에 존재하는 중복 단어들을 제거한다.

words.sort() # 일단 문자열을 정렬 해주고 난 다음
words.sort(key=len) # 그 다음에 길이 순으로 정렬해준다. / key=len은 길이를 기준으로 정렬한다는 의미

# print(words)
for i in words:
    print(i)

"""
길이가 짧은 것부터
길이가 같으면 사전 순으로
중복된 단어는 하나만 남기고 제거해야 한다.
첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 
둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 
주어지는 문자열의 길이는 50을 넘지 않는다.
"""