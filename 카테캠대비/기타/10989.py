# 10989 : 수 정렬하기 3
# https://www.acmicpc.net/problem/10989
# 카운팅 정렬? https://seongonion.tistory.com/130
# 시간 복잡도를 지금까지 고려했었는데, 이제 메모리 초과도 고려해야 한다.
# sys,stdin.readline(시간 복잡도 개선) + 계수 정렬(메모리 사용량 개선) 사용이 관건!

import sys

N = int(sys.stdin.readline()) # 입력받을 수의 개수

count = [0] * 10001 # 중복이 될 수 있다는 점을 이용하여 계수 정렬을 사용한다.
# 입력으로 받을 수 있는 10000까지의 수를 담을 수 있는 배열을 만든다
# 입력받을 때 마다 해당 수에 맞는 인덱스에 +1을 해줘서 그 수의 개수를 담는다.
# 입력이 모두 끝난 후 배열을 돌면서 어떤 인덱스의 값이 0이 아니라면 인덱스에 해당하는 숫자만큼 숫자를 출력
# 이렇게 하면 정렬이 자연스럽게 되는 모습을 확인할 수 있다.

# for문 속에서 append를 사용하면, 메모리 재할당이 이루어져서 메모리를 효율적으로 사용 불가능.
# 입력값이 극한으로 많이 주어질 때에는 메모리를 좀 더 효율적으로 사용해야 한다.
for i in range(0, N):
    number = int(sys.stdin.readline()) # 매 줄마다 숫자를 입력 받는다.
    count[number] += 1 # 숫자에 해당하는 인덱스의 카운트를 +1
    # numbers.append(int(sys.stdin.readline()))

for i in range(10001):
    for j in range(count[i]): # count배열의 i번째 인덱스에 대해서
        print(i)