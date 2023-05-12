# 2439 : 별 찍기 - 2

numbers = int(input())

for i in range(1, numbers+1):
    print(" " * (numbers-i), end="") # end를 쓰면, 그 뒤의 출력값을 이어서 출력(줄바꿈을 하지 않는다!)
    print("*" * i)

"""
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
"""