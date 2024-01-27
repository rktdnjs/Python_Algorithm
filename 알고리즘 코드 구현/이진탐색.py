# 재귀 함수 이진탐색
# 해당하는 원소를 찾았을 경우 그 인덱스 반환
def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    # 만약 중간 값이 찾으려는 값보다 크면 중간에서 좌측 확인
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    # 만약 중간 값이 찾으려는 값보다 작으면 중간에서 우측 확인
    else:
        return binary_search(arr, target, mid + 1, end)
    
# 원소의 개수 & 찾고자 하는 데이터 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 arr 입력받기
arr = list(map(int, input().split()))

# 이진 탐색 수행 결과
res = binary_search(arr, target, 0, n - 1)
if res == None:
    print("찾으려는 원소가 존재하지 않습니다")
else:
    print(res + 1)

# ----------------------------------------- # 

# 반복문 이진탐색
def bin_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None

# 원소의 개수 & 찾고자 하는 데이터 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 arr 입력받기
arr = list(map(int, input().split()))

# 이진 탐색 수행 결과
res = binary_search(arr, target, 0, n - 1)
if res == None:
    print("찾으려는 원소가 존재하지 않습니다")
else:
    print(res + 1)