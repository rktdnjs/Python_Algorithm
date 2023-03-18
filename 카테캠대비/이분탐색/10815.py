# 10815 : 숫자 카드
# https://www.acmicpc.net/problem/10815

# 시간을 해결해야하기 때문에, count를 사용하는 것은 좋은 방법이 아니다.
# 리스트에 어떤 요소가 몇 개 있는지, 그 부분에서 시간을 최소화해야한다.

# 해쉬
# 해쉬 자료구현은 보통 파이썬의 자료구조 중 하나인 딕셔너리를 사용한다.
# hash 맵에서 해당 주소에 값이 있을 경우, 해당 값에 추가하며
# hash 맵에서 해당 주소에 값이 없을 경우, 값을 새로 추가한다.
# 해쉬 방식을 이용하여 cards를 순회하면서 해당 값이 없으면 해쉬맵에 새로 추가하고, 이미 있다면 값을 1증가.
# 이렇게 쓱쓱 세다보면 우리가 만든 hashamp에는 모든 요소들의 숫자가 세어져있고, 이를 사용! 

# Counter 함수(개수 셀 때 유용!) - https://www.daleseo.com/python-collections-counter/
# 중복된 데이터가 저장된 리스트를 인자로 넘기면, 각 원소가 몇 번 나오는지 저장된 객체를 얻는다.
# Counter 클래스는 파이썬의 자료구조 중 하나인 딕셔너리를 확장하고 있기에, 그와 관련된 API사용가능!

# 참고 : https://blockdmask.tistory.com/468 (파이썬 .join 함수)

import sys
from collections import Counter

input = sys.stdin.readline

N = int(input()) # 보유하고 있는 숫자 카드의 개수
cards = list(map(int, input().split()))
M = int(input()) # 몇 개 보유하고 있는지 궁금한 카드의 수
cards_want = list(map(int, input().split()))

card_list = Counter(cards)

for card in cards_want:
    if card in card_list:
        print(1, end=' ')
    else:
        print(0, end=' ') 

"""
[Counter 함수 사용해서 푸는 방법]
card_list = Counter(cards) # 보유하고 있는 카드가 몇 개씩 있는지 Counter 함수를 통해 얻는다. 

for card in cards_want:
    if card in card_list:
        print(card_list[card], end=' ')
    else:
        print(0, end=' ')
"""