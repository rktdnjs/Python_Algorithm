numbers = int(input())

for i in range(1, numbers+1):
    print(" " * (numbers-i), end="")
    print("*" * i)