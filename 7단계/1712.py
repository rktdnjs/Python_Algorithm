# 1712 : 손익분기점
# https://www.acmicpc.net/problem/1712
# A, B, C가 빈칸을 두고 차례대로 입력
# A + B * x < C * x 인 x를 구해야한다.
# A < (C - B) x 
# 근데, 손익분기점이 존재하지 않을경우, 즉 구할수 없을 때는 -1을 출력한다.
# 손익분기점이 존재하지 않는다는 것은, C - B의 값이 음수가 나올 경우임!

# count를 주고 사용했더니 시간 초과가 떴다. 좀 더 코드를 간결화 해봐야 할 듯..
# 차라리 x 를 한쪽 변에 놔두고 나머지를 모두 이항하여 정리?
# A // (C - B)로 계산하는 경우, 런타임 에러가 발생하였다. 그 이유는, C == B 인 케이스가 존재하기 때문인듯


A, B, C = map(int, input().split()) # A(고정비용), B(가변비용), C(상품가격)를 입력받는다.

if(C-B < 0):
    print(-1) # 손익분기점이 존재할 수 없음

else:
    try:
        print(A//(C-B) + 1) # / 연산자를 사용하면 소수점이 나옴.
    except ZeroDivisionError: # B == C인 경우에 생기는 에러 예외 처리 -> 다시 생각해보니 그냥 위에 if 조건문을 등호 포함하면 되지 않을까 싶다..!
        print(-1)

"""
예를 들어 A=1,000, B=70이라고 하자. 이 경우 노트북을 한 대 생산하는 데는 총 1,070만원이 들며, 
열 대 생산하는 데는 총 1,700만원이 든다.
산 대수를 늘려 가다 보면 어느 순간 총 수입(판매비용)이 총 비용(=고정비용+가변비용)보다 많아지게 된다.
최초로 총 수입이 총 비용보다 많아져 이익이 발생하는 지점을 손익분기점이라 한다.
A, B, C가 주어졌을 때, 손익분기점을 구하는 프로그램을 작성하시오.

첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 21억 이하의 자연수이다.

첫 번째 줄에 손익분기점 즉 최초로 이익이 발생하는 판매량을 출력한다. 
손익분기점이 존재하지 않으면 -1을 출력한다.
"""