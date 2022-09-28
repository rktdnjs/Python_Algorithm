# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
# 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.

input()
l = list(map(int, input().split())) # 정수 입력을 스페이스바를 기준으로 나눠 받음
min, max = 1000000, -1000000 # 최대 최소 값(값을 갱신할 수 있게 리버스로 둠)

for item in l: #해당 리스트의 아이템들에 대해서 
  if item > max: #어떤 아이템이 max보다 넘는지 확인, 갱신
    max = item
  if item < min: #어떤 아이템이 min보다 작은지 확인, 갱신
    min = item

print(min, max)