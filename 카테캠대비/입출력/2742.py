# 2742 : 기찍 N
# https://www.acmicpc.net/problem/2742

import sys

N = int(sys.stdin.readline().strip())

for i in range(N, 0, -1):
    print(i)

"""
for i in reversed(range(Input)):
    print(i + 1)

# reversed를 사용하면 리스트의 원소를 거꾸로 뒤집어서 이를 반환함
# range()는 파라미터 start, step은 생략 가능하며 생략할 시 0, 1로 주어진다.
# range([start] stop [step])의 형태로 구성됨
# 만약 step을 -1로 주게되면, 거꾸로 출력됨
"""