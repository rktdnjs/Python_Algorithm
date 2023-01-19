numbers = int(input())

for i in range(1, numbers+1):
    print(" " * (numbers-i), end="") # end를 쓰면, 그 뒤의 출력값을 이어서 출력(줄바꿈을 하지 않는다!)
    print("*" * i)