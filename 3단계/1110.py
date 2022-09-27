N = int(input())
num = N
count = 0

while True:
    a = num // 10 # //는 나누기 연산 후 소수점 이하의 수를 버림. 즉 정수 부분의 몫을 구함
    b = num % 10 # %는 나누기 연산 후 몫이 아닌 나머지를 구함
    c = (a + b) % 10 # 그리고 해서 나온 결과를 더한다음 오른쪽 숫자를 구해주고
    num = (b * 10) + c # 기존에 있던 오른쪽 숫자를 십의 자리로 하는 새로운 수를 구함

    count = count + 1 # 이 과정을 반복할 때마다 카운트가 증가
    if(num == N): # 만약 이 과정을 반복하던 중에 처음의 숫자 N이 나오게 되면 break!
        break

print(count)