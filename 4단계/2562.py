"""
9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 
그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
예를 들어, 서로 다른 9개의 자연수
3, 29, 38, 12, 57, 74, 40, 85, 61
이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.
"""

num_list = [] # 빈 배열 생성

for i in range(0, 9): # 9번 반복
    num_list.append(int(input())) # 숫자를 입력받아서 int형으로 numlist에 추가함

max_num = -1000000 # 최대 최소 값(값을 갱신할 수 있게 리버스로 둠)

for item in num_list : # 해당 리스트의 아이템들에 대해서 
  if item > max_num: # 어떤 아이템이 max_num 보다 넘는지 확인, 갱신
    max_num = item

print(max(num_list)) # max()함수를 사용하여 num_list의 최대값을 출력가능하다.
print(num_list.index(max(num_list))+1) 
# num_list의 번호를 출력하는데 위치는 index함수를 이용해서 찾는다.
# 이때 max()를 이용하여 max가 해당하는 위치의 인덱스에 1을 더함
# (인덱스가 0부터 시작하기 때문)
