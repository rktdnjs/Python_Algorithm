# 1037 : 약수
# https://www.acmicpc.net/problem/1037

# def GCD(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a

N = int(input())

factors = list(map(int, input().split()))

A = max(factors)
B = min(factors)
print(A * B)

# if length == 1:
#     print(factors[0]*2)
# else:
#     factors.sort()
#     print(factors[0] * factors[-1])
    # A = factors[-1]
    # B = factors[-2]
    # gcd = GCD(A, B)
    # lcm = int(A*B/gcd)
    # if lcm == A:
    #     print(2*lcm)
    # else:
    #     print(lcm)
