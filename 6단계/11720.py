# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.
# input으로 받아온 값을 list에 저장하면 자동으로 구분되어짐(1자리 숫자)을 이용

Num = int(input()) # 몇 개의 수를 입력할 것인가?
numbers = list(input()) # 입력받은 수를 공백구분없이 분리 시키기 위해 list사용
total = 0

for i in numbers:
    total += int(i)

print(total)