a, b, c, d, e, f = map(int, input().split())

# 그냥 모든 케이스에 대해서 쭉 돌리다가 이에 맞는 x y 가 등장하면 그 x y 를 출력하고 끝냄
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x + b*y == c and d*x + e*y == f:
            print(x, y)
            break