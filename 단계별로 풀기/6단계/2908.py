"""
두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오.
"""

numbers = list(input().split())
A = numbers[0] # 입력된 두 수를 각각의 변수에 저장, 나중에 역순으로 슬라이싱 하기 위함
B = numbers[1]

A = A[::-1] # 각 수를 역순으로 다시 배치하여 변수에 저장 이후 이제 크기 비교 진행
B = B[::-1]

if A < B :
    print(B)
else : 
    print(A)