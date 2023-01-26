# 2775 : 부녀회장이 될테야
# https://www.acmicpc.net/problem/2775
# k층의 n호에 몇 명이 살고 있는지에 대해서 출력.
# 0층의 i호에는 i명이 산다!
# 예를 들어, 1층의 3호에 살기 위해서는 0층의 3호까지, 1+2+3 명이 필요.
# 예를 들어, 2층의 3호에 살기 위해서는 1층의 3호까지, 참고로 1층의 1호에는 1명 1층의 2호에는 1+2=3명
# 따라서 1+3+6=10명이 2층의 3호에 거주한다.
# 규칙을 찾아서 그에 대해서 사는 사람의 수를 출력해내면 될 듯!

# 추후, 리스트 컴프리핸션에 대해서 찾아보면 도움이 될 듯 하다.

"""
3층 1 5 15 35 70
2층 1 4 10 20 35
1층 1 3 6  10 15
0층 1 2 3  4  5
k층 1 2 3 4호 기준으로 차례차례 봐보자.
1 2 3 4     
1 3 6 10
+1 +1 +1
+2 +3 +4
+3 +6 +10
+4 +10 +20
"""

T = int(input()) # 테스트 케이스의 수

for i in range(0, T): # k-1층의 n호까지의 합을 구해서 출력해야함.
    k = int(input()) # k층
    n = int(input()) # n호
    
    apart = [[0 for j in range(n)] for i in range(k+1)] # 2차원 리스트 생성
    # 0 for j in range(k)를 통해서 0을 k번 반복한 리스트를 만드는 작업을 i in range(n)을 통해 n번 반복한다.
    # 이렇게 하면 n * k 배열이 생성된다.
    # 우리가 원하는 것은 k(층) * n(호) 배열이므로, 위치를 바꿔준다.
    #print(apart) 2차원 리스트 형태 확인용

    for y in range (0, k+1): # 층 (0~k층까지)
        for x in range (0, n): # 호(1~n호까지)
            if(y==0): # 0층일 경우
                apart[0][x] = 1 + x
            elif(x==0): # 각 층의 1호일 경우
                apart[y][0] = 1
            else:
                apart[y][x] = apart[y][x-1] + apart[y-1][x]
    print(apart[y][x])
    # print(apart)

"""
첫 번째 줄에 Test case의 수 T가 주어진다.
그리고 각각의 케이스마다 입력으로 첫 번째 줄에 정수 k, 두 번째 줄에 정수 n이 주어진다

각각의 Test case에 대해서 해당 집의 거주민 수를 출력하라.
"""

"""
찾아보니까 이렇게도 풀 수 있었다.
t = int(input())

for _ in range(t):  
    floor = int(input())  # 층
    num = int(input())  # 호
    f0 = [x for x in range(1, num+1)]  # 0층 리스트 -> 리스트 컴프리핸션 표현 사용 
    # 1 ~ n 호에 대한 인덱스 생성, index = 0 ~ num-1 까지 생김

    for k in range(floor):  # 층 수 만큼 반복
        for i in range(1, num):  # 1 ~ n-1까지 (인덱스로 사용)
            f0[i] += f0[i-1]  # 층별 각 호실의 사람 수를 변경
    print(f0[-1])  # 가장 마지막 수 출력

"""