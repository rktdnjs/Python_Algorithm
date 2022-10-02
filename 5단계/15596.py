"""
정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오.
* 파이썬 * 
a: 합을 구해야 하는 정수 n개가 저장되어 있는 리스트 
(0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)
리턴값: a에 포함되어 있는 정수 n개의 합 (정수)
"""

def solve(a): # 그냥 이렇게 하면 끝임
    return sum(a)


""" 입력 값이 따로 필요 없었다...(머쓱^^;)
def func(numbers): # numbers(매개변수, 리스트)를 넘겨 받음, 이때 함수의 이름은 func로 정의함
    result = sum(numbers)
    return result

a = list(map(int, input().split())) # 스페이스바를 기준으로 나눠서 값을 받음, int데이터를 지닌 리스트로 변환
print(func(a)) # 함수 호출, 합을 구하기 위한 함수 func를 호출
"""