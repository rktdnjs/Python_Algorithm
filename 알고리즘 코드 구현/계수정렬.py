# 계수 정렬(Count Sort)
# 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 주로 사용
# 계수 정렬의 시간 복잡도 : O(N+K)(K:데이터 중 최대값의 크기)

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 모든 범위를 포함하는 리스트 선언(모든 값을 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값을 증가시킴

# 계수정렬된 리스트 출력
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')