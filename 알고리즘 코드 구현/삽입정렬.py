# 삽입 정렬(Insertion Sort)
# 데이터를 하나씩 확인하며 각 데이터를 적절한 위치에 삽입하는 알고리즘
# 삽입 정렬은 2번째 데이터부터 시작함. 1번째 데이터는 그 자체로 정렬되어 있다고 판단하기 때문!
# 시간 복잡도 N(O^2), 최선의 경우 O(N)
# 삽입 정렬은 정렬이 거의 되어있는 상태에서 매우 강력함!

import time # 시간 측정용

start_time = time.time() # 측정 시작

array = [5, 1, 7, 9, 10, 2, 4, 3, 8, 6]

for i in range(1, len(array)): # 삽입 정렬은 2번째 데이터부터 시작함. 1번째 데이터는 그 자체로 정렬되어 있다고 판단하기 때문!
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 감소하며 반복하는 문법
        if array[j] < array[j - 1]: # 왼쪽보다 오른쪽이 클경우, 1칸씩 왼쪽으로 이동한다.
            array[j], array[j - 1] = array[j - 1], array[j]
        else: # 왼쪽 숫자와 비교하다가 왼쪽이 자신보다 작을 경우 해당 위치에서 멈춘다.
            break

print(array)

# 프로그램 소스 코드
end_time = time.time() # 측정 종료
print("걸린 시간 : ", end_time - start_time) # 수행 시간 출력