# 퀵 정렬(Quick Sort)
# 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 정렬
# 퀵 정렬에서는 피벗(pivot, 기준)이 사용된다.
# 피벗을 설정하고 리스트를 분할하는 방법에 따라서 여러 가지 방식으로 퀵 정렬을 구분함
# 여기서는 가장 대표적인 분할 방식인 호어 분할 방식을 기준으로 퀵 정렬 구현

# 호어 분할 : 리스트에서 1번째 데이터를 피벗으로 정함
# 피벗을 설정한 다음에는 왼쪽에서부터 피벗보다 큰 데이터를 찾고, 오른쪽에서부터 피벗보다 작은 데이터를 찾음
# 데이터의 위치가 엇갈리기전까지 발견되는 숫자끼리 두 데이터의 위치를 서로 변경한다.
# 만약 찾은 두 값이 엇갈린 경우에는 '작은 데이터' <-> '피벗' 이렇게 위치를 변경한다.
# 이렇게 하면 피벗의 왼쪽에는 피벗보다 작은 데이터 / 피벗의 오른쪽에는 피벗보다 큰 데이터가 존재하는 형태가 된다!
# 이제 이렇게 나누어진 리스트에 대해서 각각 피벗을 다시 설정하여 동일한 방식으로 정렬 수행

# 퀵 정렬이 끝나는 조건 : 현재 리스트의 데이터 개수가 1개인 경우
# 코드를 보며 이해해 보자!

import time # 시간 측정용

# 퀵 정렬 함수 구현
def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료한다.
        return
    pivot = start # 맨 처음, 피벗은 1번째 원소로 설정
    left = start + 1 # 왼쪽과 오른쪽 위치를 세팅함
    right = end

    while left <= right: 
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        # left <= end 이면서, 아직 피벗보다 큰 숫자를 발견하지 못했다면 left를 오른쪽으로 한 칸씩 옮김
        while left <= end and array[left] <= array[pivot]:
            left += 1
        
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        # left <= end 이면서, 아직 피벗보다 작은 숫자를 발견하지 못했다면 right를 왼쪽으로 한 칸씩 옮김
        while right > start and array[right] >= array[pivot]:
            right -= 1
        
        if left > right: # 만약 위에서 찾은 데이터들이 양쪽에서 오다가 엇갈렸다면, 작은 데이터와 피벗을 교체함!
            array[right], array[pivot] = array[pivot], array[right]
        
        else: # 엇갈리지 않았다면, 작은 데이터와 큰 데이터의 위치를 교체
            array[left], array[right] = array[right], array[left]
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    # 엇갈렸을 경우 right의 위치와 pivot이 바뀌기 때문에 right의 앞쪽 뒤쪽을 기준으로 끝점을 세팅하여 다시 퀵 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)
    
start_time = time.time() # 측정 시작

array = [5, 1, 7, 9, 10, 2, 4, 3, 8, 6]

quick_sort(array, 0, len(array) - 1) # 시작 0번 인덱스 / 1을 빼주어야 배열의 인덱스와 딱 맞음

print(array)

# 프로그램 소스 코드
end_time = time.time() # 측정 종료
print("걸린 시간 : ", end_time - start_time) # 수행 시간 출력