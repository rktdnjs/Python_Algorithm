# N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

A, B = [], [] # 두 행렬 A와 B를 선언해준다.

N, M = map(int, input().split()) # N * M이 어떤 크기인지 입력받는다.

for row in range(N): # 행의 개수 만큼 입력 받는다
    row = list(map(int, input().split())) # 공백을 구분해서 받는 통째로 int를 했더니 오류가 발생. 각각에 int를 적용함
    A.append(row) # 해당 행을 A에 추가

for row in range(N):
    row = list(map(int, input().split())) # 위와 동일
    B.append(row) # 해당 행을 B에 추가

for row in range(N):
    for column in range(M): # N * M 개수만큼 반복하여 각 항들끼리 합해서 빈 칸 출력후 계속 넘어감!
        print(A[row][column] + B[row][column], end = ' ' )
    print()