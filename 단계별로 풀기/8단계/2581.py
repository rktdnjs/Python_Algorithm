# 2581 : 소수
# https://www.acmicpc.net/problem/2581
# 주의!!!!!!!! : 리스트 remove 사용 시 조심할 점 https://taylor-kang.tistory.com/12
# 소수의 합과, 최솟값을 찾아서 출력한다.
# 소수에 대한 리스트를 구해서, 해당 리스트들에 대해서 소수를 구한다.

M = int(input()) # 최소값 입력
N = int(input()) # 최대값 입력

num_list = [x for x in range(M, N + 1)] # M이상 N이하의 자연수들에 대해서 리스트를 생성한다.
# print(num_list) 체크용

for num in num_list[:]: # 복사한 리스트에 대해서(인덱스 관련 문제 방지)
    if num == 1: # 이 친구는 소수가 아님
        num_list.remove(1)
    else:
        for i in range(2, num) : # 2 ~ num-1 까지의 숫자들로 전부 나눠본다.
            if num % i == 0 : # 만약 나눠지는게 있을 경우, 해당 숫자는 소수가 아님
                num_list.remove(num)
                break

if len(num_list) < 1: # 만약 구해본 소수 리스트에 아무것도 없다면
    print(-1)
else: # 소수 리스트에 무엇인가 있다면
    print(sum(num_list))
    print(min(num_list))



"""
입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.
M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.

M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력
단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력
"""