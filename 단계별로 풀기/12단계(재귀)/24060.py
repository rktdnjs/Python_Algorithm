# 24060 : 병합 정렬 1
# https://www.acmicpc.net/problem/24060
# 병합 정렬 구현 + 언제 데이터가 업데이트 되는지
# 배열을 더 이상 나눌 수 없을 때 까지 분할 + 다시 병합하면서 점점 큰 배열을 만들어 나간다.
# 참고로, 병합 정렬(Merge Sort)의 경우 시간 복잡도는 O(NlogN)이다.

import sys

def merge_sort(L): # 입력받은 배열을 오름차순 정렬한다.
    if len(L) == 1 : # 더 이상 배열이 나누어 지지 않는경우
        return L # 그대로를 반환
    
    mid = (len(L) + 1) // 2 # 배열의 중간 지점을 구하기 위해서 배열의 길이를 2로 나누어준다. 단, 이 문제의 경우 앞 배열의 길이가 크도록 병합하기 때문에 +1을 해준다.
    left = merge_sort(L[:mid]) # 중간 지점을 기준으로 mid 전 까지를 잘라낸다. (파이썬 슬라이싱에서 :end의 경우 end 자체는 포함하지 않는다.
    right = merge_sort(L[mid:]) # 중간 지점을 기준으로 mid 부터 끝 까지 잘라낸다.

    merged_arr = [] # 병합완료된 배열을 담기 위한 임시 공간을 생성한다.
    l, h = 0, 0 # 나누어진 배열에 대해서 병합을 진행하기 위한 임시 변수(인덱스 용) 선언, 맨 처음 인덱스부터 정렬 시작

    while l < len(left) and h < len(right): # 각각의 배열의 길이를 초과하기 전까지 진행(단, 한 쪽이 전부 추가되어 종료되었을 시 다음 while문으로 이동하여 계속 병합 진행)
        if left[l] < right[h]: # 만약 좌측 배열의 원소가 우측 배열의 원소보다 작을 경우
            merged_arr.append(left[l]) # 병합 배열에 좌측 배열의 원소(작은 친구)를 쏙 넣어준다.
            merge_tem.append(left[l]) # <- 얘는 도대체 왜 쓰냐? 바로 추가되는 순서와 카운트를 편하게 세기 위해서 그렇다.
            # merge_process에 추가되는 순서대로 그 때 그 때 추가되는 원소를 출력할 수도 있고, 총 인덱스의 개수가 저장 횟수가 되는 것과 마찬가지이다.
            l += 1 # 그리고 l은 오른쪽으로 한 칸 이동한다.
        else: # 만약 우측 배열의 원소가 좌측 배열의 원소보다 작을 경우
            merged_arr.append(right[h]) # 병합 배열에 우측 배열의 원소(작은 친구)를 쏙 넣어준다.
            merge_tem.append(right[h])
            h += 1 # 그리고 h는 오른쪽으로 한 칸 이동한다.
    
    while l < len(left): # 좌측 배열의 원소가 아직 남아있을 경우, 해당 원소들에 대해서 계속 병합 진행
        merged_arr.append(left[l])
        merge_tem.append(left[l])
        l += 1
    
    while h < len(right): # 우측 배열의 원소가 아직 남아있을 경우, 해당 원소들에 대해서 계속 병합 진행
        merged_arr.append(right[h])
        merge_tem.append(right[h])
        h += 1

    return merged_arr

N, K = map(int, sys.stdin.readline().split()) # N(배열 A의 원소 수) & K(저장 횟수)
A = list(map(int, sys.stdin.readline().split())) # 배열 A를 입력받는다.

merge_tem = []

merge_sort(A)

# print(merge_tem)

if len(merge_tem) >= K: # 만약 결과로 얻은 merge_tem의 인덱스(저장 횟수)가 K보다 크거나 같으면 특정 저장횟수번째에 해당하는 원소를 출력해준다.
    print(merge_tem[K-1])
else: # 만약 설정한 저장횟수보다 적을 경우, -1을 출력하고 종료한다.
    print(-1)