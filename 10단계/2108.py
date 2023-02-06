# 2108 : 통계학
# https://www.acmicpc.net/problem/2108
# 시간초과 이슈 ㅎㅎ;;
# sys,stdin.readline(시간 복잡도 개선)를 사용하면 입력받는 시간을 줄일 수 있다. - 개행문자 제거!
# Counter 함수를 통해 가장 많이 나오는 데이터를 찾을 수 있다. 
# Counter 함수의 most_common()함수의 결과값은 Tuple 자료형이다.
 
from collections import Counter # Counter 함수 import - 최빈값을 찾기 위한 내장 라이브러리
import sys

N = int(sys.stdin.readline()) # 입력받을 수의 개수

number = []

for i in range(0, N):
    number.append(int(sys.stdin.readline()))

number.sort() # 오름차순 정렬

# 산술평균
print(round(sum(number) / N))

# 중앙값
# 인덱스의 길이가 짝수인지, 홀수인지에 따라 나눔
# 아차차 ㅎㅎ;; 나중에 다시 보니 홀수개만 받는다는 가정이 있었다!(짝수개 고려 x)
# length = len(number) -> 맨 처음에 받았던 N 그냥 사용해서 연산량 줄임
print(number[N//2])

# 최빈값 - Counter 함수 사용!
# 반환형이 Tuple이라, 자료형태를 보면 리스트안에 튜플이 있는 [(),()...]형태가 된다.
# 이 상태에서 접근할 때는 그냥 2차원 리스트로 접근하는 것과 똑같이 생각하면 OK.
most = Counter(number).most_common() # 데이터의 개수가 많은 순으로 정렬된 배열을 most에 리턴한다.
if len(most) == 1: # 만약에 1개만 입력받는 경우, 해당 조건이 있어야 함
    print(most[0][0])
elif most[0][1] == most[1][1]: # 최빈값의 목록이 2개 이상 존재할 경우, 2번째로 작은 값을 출력한다.
    print(most[1][0])
else:
    print(most[0][0])

# 범위
print(max(number) - min(number))

"""
N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.
산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이

첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 단, 'N은 홀수'
입력되는 정수의 절댓값은 4,000을 넘지 않는다.
"""