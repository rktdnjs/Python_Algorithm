# 1978 : 소수 찾기
# https://www.acmicpc.net/problem/1978

N = int(input()) # 입력은 받는데 
count = 0

num_list = list(map(int, input().split())) # 숫자들을 전부 입력 받아서 리스트 형태로 저장

for num in num_list:
    if num == 1:
        continue

    if num == 2: # 2는 소수이므로 카운트 증가
        count +=1
        continue

    else:
        sosu = 0
        for i in range(2, num) : # 2 ~ num-1 까지의 숫자들로 전부 나눠본다.
            if num % i == 0 : # 만약 나눠지는게 있을 경우, 해당 숫자는 소수가 아님
                sosu -= 1
                continue  
        if sosu == 0 :
            count += 1
            
print(count)



"""
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
주어진 수들 중 소수의 개수를 출력한다.
"""