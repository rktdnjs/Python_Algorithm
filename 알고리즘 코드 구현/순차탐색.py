# 순차 탐색 소스코드
def sequential_search(n, target, arr):
    # 각 원소 하나씩 확인
    for i in range(n):
        if arr[i] == target:
            return i + 1

print("원소 개수와 찾으려는 데이터 입력")
input_data = input().split()
n = int(input_data[0]) # 원소의 개수
target = input_data[1] # 찾으려는 문자열

print("원소의 개수 만큼 데이터 입력. 구분은 띄어쓰기 1칸")
arr = input().split()

# 순차 탐색 수행 결과
print(sequential_search(n, target, arr))