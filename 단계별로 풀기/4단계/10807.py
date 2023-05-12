# 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.

# 첫째 줄에 정수의 개수 N(1 ≤ N ≤ 100)이 주어진다. 
# 둘째 줄에는 정수가 공백으로 구분되어져있다. 
# 셋째 줄에는 찾으려고 하는 정수 v가 주어진다. 
# 입력으로 주어지는 정수와 v는 -100보다 크거나 같으며, 100보다 작거나 같다.

# 첫째 줄에 입력으로 주어진 N개의 정수 중에 v가 몇 개인지 출력한다.

numbers_count = int(input()) # 입력할 숫자의 개수
numbers = list(map(int, input().split())) # 입력한 숫자를 공백을 기준으로 나눠 받음
number_target = int(input()) # 찾을 숫자를 입력 받는다.
count = 0

for i in numbers :
    if i == number_target :
        count += 1

print(count)


# 아래 처럼 하는 방법도 있었다.
# N = int(input())
# N_list = list(map(int, input().split()))
# v = int(input())
# print(N_list.count(v))