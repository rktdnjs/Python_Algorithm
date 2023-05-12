# 11021 : A+B - 7

import sys
test = int(input())
# 한 줄에 여러 함수 입력 받기 가능
# 기본적으로 readline()은 줄 바꿈 문자를 포함하고 있다.
for i in range(1, test+1):
    a, b = map(int, sys.stdin.readline().split())
    print(f'Case #{i}: {a+b}')

# 파이썬에서 가장 자주 쓰는 입력 함수는 input()이 있다.
# 하지만 입력 값을 수 백, 수 천개 받을 때는, 입출력 속도를 위해서 
# sys.stdin 함수를 사용해주는 것이 더 좋다.
# 파이썬 알고리즘 문제를 풀때, 시간초과 에러가 나오는 경우 해결 방법이기도 하다!
# import sys를 사용해보자!