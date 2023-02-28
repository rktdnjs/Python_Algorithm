# 18870 : 좌표 압축
# https://www.acmicpc.net/problem/18870

import sys

N = int(sys.stdin.readline()) # 입력받을 좌표의 개수

numbers = []
numbersDic = {}

numbers = list(map(int, sys.stdin.readline().split()))

sortNumbers = sorted(list(set(numbers))) # 중복 제거 & 오름차순 정렬



for i in range(len(sortNumbers)):
    numbersDic[sortNumbers[i]] = i 
# 예를 들어 2 4 6 8 10이 들어간다고 할 때,
# {2 : 0, 4 : 1, ... 이런식으로 자료가 들어간다, 즉 숫자와 그에 해당하는 인덱스가 들어간다!}

for i in numbers:
    print(numbersDic[i], end=' ') # 숫자에 해당하는 자료를 바로 쏙 찾아내어 인덱스를 출력한다.

# 문제가 되는 코드, list.index(i)의 경우 시간복잡도 O(N)이기 때문에 시간초과가 발생한다.
# 따라서 시간 복잡도 O(1)인 index[i]를 사용하는 딕셔너리 자료형을 사용해준다.
"""
for i in numbers:
    print(sortNumbers.index(i), end=' ')
"""


"""
첫째 줄에 N이 주어진다.
둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.
"""