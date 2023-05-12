# 선택 정렬(Selection Sort)
# 매 번 가장 작은 것을 선택해서 가장 앞으로 보내는 정렬
# 시간 복잡도 O(N^2)

import sys
import time # 시간 측정용

start_time = time.time() # 측정 시작

array = [1, 5, 7, 9, 10, 2, 4, 3, 8, 6]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스 -> 0, 1, 2, 3, ... 9
    for j in range(i + 1, len(array)): # 0, 1, 2, 3, ... 9 부터 시작해서 끝 까지 비교
        if array[j] < array[min_index]: # 만약 더 작은 원소가 비교중에 존재한다면!
            min_index = j # j 의 값으로 min_index를 업데이트
    array[i], array[min_index] = array[min_index], array[i] # 발견된 가장 작은 원소와 i번째 자리의 원소와 자리 변경(업데이트)

print(array)

# 프로그램 소스 코드
end_time = time.time() # 측정 종료
print("걸린 시간 : ", end_time - start_time) # 수행 시간 출력