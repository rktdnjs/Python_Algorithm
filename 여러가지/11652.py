# 11652 : 카드
# https://www.acmicpc.net/problem/11652

import sys

input = sys.stdin.readline

# int형으로 바꾸어서 받아주면, 굳이 개행문자를 따로 처리하지 않아도 삭제된다.
# 그냥 아래처럼 사용해도 OK임
N = int(input())

cards = {}

for i in range(N):
    new_card = int(input())
    if new_card in cards : # 카드 딕셔너리에 이미 존재하는 카드라면, 해당 key에 대한 value를 1증가
        cards[new_card] += 1
    else : # 카드 딕셔너리에 없는 카드라면, 새로 추가하며 value를 1로 세팅
        cards[new_card] = 1

# 딕셔너리의 key를 정렬하는 방법은, items메서드를 사용한다. -> dic.items()
# value(개수)에 대해서 내림 차순 정렬한 후(많은 것이 앞에오도록)
# 이후 카드 개수가 같으면 카드에 적힌 정수가 가장 작은것이 앞에오도록 오름차순 정렬한다.

result = sorted(cards.items(), key = lambda x : (-x[1], x[0]))
# print(result)
print(result[0][0])