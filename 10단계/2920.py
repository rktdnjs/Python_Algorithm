"""
다장조는 c d e f g a b C, 총 8개 음으로 이루어져있다. 
이 문제에서 8개 음은 다음과 같이 숫자로 바꾸어 표현한다. 
c는 1로, d는 2로, ..., C를 8로 바꾼다.
1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 
둘 다 아니라면 mixed 이다.
연주한 순서가 주어졌을 때, 이것이 ascending인지, descending인지, 
아니면 mixed인지 판별하는 프로그램을 작성하시오.
"""

# 파이썬에서 sort : 정렬, 기본값은 오름차순 정렬이다.
# reverse 옵션을 주면 내림차순 정렬을 수행한다. 이 때 reverse=True 이다.
# 정렬된 결과를 반환하는 함수는, 원본을 변형하지 않기 때문에 수행한 결과를 따로 저장!

input = list(map(int, input().split()))

if input == sorted(input): # 만약 입력받은것과 정렬한 것이 같으면 오름차순
    print("ascending")
elif input == sorted(input, reverse = True): # 만약 내림차순 정렬한 것과 같으면 다음과 같이 출력
    print("descending")
else:
    print("mixed")