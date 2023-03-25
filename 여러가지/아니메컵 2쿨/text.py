import time

start_time = time.time()

N, M = map(int, input().split())
pages = list(map(int, input().split()))

# 중복된 페이지 제거 후 정렬
unique_pages = sorted(list(set(pages)))
# 첫 번째 페이지와 마지막 페이지 추가
unique_pages = [1] + unique_pages + [N]
# 잉크 사용량 초기화
ink_usage = 0

for i in range(len(unique_pages) - 1):
    # 현재 페이지와 다음 페이지 간의 차이
    diff = unique_pages[i+1] - unique_pages[i] + 1
    # 연속된 페이지가 아니라면
    if diff <= 5:
        ink_usage += 2 * diff - 1
    # 연속된 페이지라면
    else:
        ink_usage += 5 + 2 * (diff - 5)

print(ink_usage)
print(time.time() - start_time) # 코드 실행 시간 출력
