# 알고리즘 수업 - 피보나치 수 1
# https://www.acmicpc.net/problem/24416

N = int(input())

def fib(n):
    f = [0] * (n + 1)
    f[1] = f[2] = 1
    for i in range(3, n + 1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

def fibonacci(n):
    return n-2

print(fib(N), fibonacci(N))