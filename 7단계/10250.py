# 10250 : ACM 호텔
# https://www.acmicpc.net/problem/10250
# N번째 손님일 경우 배정되는 층은 N / H의 나머지가 된다. ex) 30 50 72 -> 72 % 30 = 12층
# 그리고 이 때 룸 번호는 N / H의 몫에 + 1을 한 값이 된다. ex) 30 50 72 -> 72 / 30 = 2에다가 + 1 = 3
# 문자열로 출력하는 것이 아니라, 숫자로 출력해야 하나?

T = int(input()) # 테스트 데이터 개수

for i in range (1, T + 1) : # 테스트 데이터 개수만큼 실행
    H, W, N = map(int, input().split()) # 호텔의 층 수, 각 층의 방 수, 몇 번째 손님인지 입력받음

    height = 0
    room = 0

    if(N % H == 0): # 만약 N이 H에 의해서 딱 나눠질 경우, 다르게 계산해주어야 한다.
        height = H
        room = N // H
        print(height * 100 + room)

    else:
        height = N % H # 몫의 나머지를 얻어서 배정될 층을 계산함
        room = N // H + 1 # 몫에다가 1을 더하여 배정될 방의 번호를 계산함
        print(height * 100 + room)


"""
프로그램은 표준 입력에서 입력 데이터를 받는다. 
프로그램의 입력은 T 개의 테스트 데이터로 이루어져 있는데 T 는 입력의 맨 첫 줄에 주어진다. 
각 테스트 데이터는 한 행으로서 H, W, N, 세 정수를 포함하고 있으며 각각 호텔의 층 수, 
각 층의 방 수, 몇 번째 손님인지를 나타낸다(1 ≤ H, W ≤ 99, 1 ≤ N ≤ H × W). 
T - 입력 테스트 데이터 수
H W N - 호텔의 층 수(H) / 각 층의 방 수(W) / 몇 번째 손님(N)

프로그램은 표준 출력에 출력한다. 각 테스트 데이터마다 정확히 한 행을 출력하는데, 
내용은 N 번째 손님에게 배정되어야 하는 방 번호를 출력한다.

[문자열로 출력 했었던 코드 ㅎㅎ;]
for i in range (1, T + 1) : # 테스트 데이터 개수만큼 실행
    H, W, N = map(int, input().split()) # 호텔의 층 수, 각 층의 방 수, 몇 번째 손님인지 입력받음

    height = 0
    room = 0

    if(N % H == 0): # 만약 N이 H에 의해서 딱 나눠질 경우, 다르게 계산해주어야 한다.
        height = H
        room = N // H
        print(str(height) + str(room))
        

    else:
        height = N % H # 몫의 나머지를 얻어서 배정될 층을 계산함
        room = N // H + 1 # 몫에다가 1을 더하여 배정될 방의 번호를 계산함

        if(room < 10):
            room = '0' + str(room) # room이 만약 한 자리 수일 경우 앞에 0을 붙여준다.
            height = str(height)
            print(height + room)

        else:
            room = str(room) # room이 만약 한 자리 수일 경우 앞에 0을 붙여준다.
            height = str(height)
            print(height + room)
"""