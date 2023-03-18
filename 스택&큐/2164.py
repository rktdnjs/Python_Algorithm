# 2164 : 카드 2
# https://www.acmicpc.net/problem/2164
# 역시나 시간 초과가 발생하였다. 
# 여러가지 자료 구조 및 정렬을 사용하여 효과적으로 시간복잡도를 줄이는 것이 중요하다...
# pop 보다는 deque(덱)을 활용한 popleft()를 사용하는 것이 시간복잡도가 많이 준다!
# 참고 : popleft - O(1) / pop - O(N)
# https://ooeunz.tistory.com/31 <- 파이썬 덱 참고하여 만듦

import sys
from collections import deque

N = int(sys.stdin.readline())

cards = deque([x for x in range(1, N+1)]) # 카드팩 생성

while len(cards) > 1: # 카드가 1장이 남을 때 까지 반복
    cards.popleft() # 맨 앞에 있는 카드를 제거
    cards.append(cards[0]) # 이후 맨 앞에 있는 카드를 맨 뒤로 추가
    cards.popleft() # 맨 앞으로부터 2번째 있는 카드를 옮겼으므로, 얘도 제거
    # print(cards)

print(cards[0]) # 마지막으로 남아있는 카드를 출력