# 1427 : 소트인사이드
# https://www.acmicpc.net/problem/1427
# 입력받을 때 str으로 입력받아 int형으로 싹둑 해서 입력받는다.
# 그리고 sort함수에서 reverse = True를 사용하여 내림차순으로 정렬한다.

numbers = list(map(int, str(input())))
numbers.sort(reverse=True)
for i in numbers:
    print(i, end='')

"""
첫째 줄에 정렬하려고 하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.
첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.
"""