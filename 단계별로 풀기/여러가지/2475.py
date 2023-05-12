# 고유번호의 처음 5자리의 숫자들이 04256이면, 각 숫자를 제곱한 수들의 합 0+16+4+25+36 = 81 을 10으로 나눈 나머지인 1이 검증수이다.
# 첫째 줄에 고유번호의 처음 5자리의 숫자들이 빈칸을 사이에 두고 하나씩 주어진다.
# 첫째 줄에 검증수를 출력한다.

input = list(map(int, input().split()))
sum = 0
result = 0

for i in input :
    sum += i * i 

result = sum % 10
print(result)