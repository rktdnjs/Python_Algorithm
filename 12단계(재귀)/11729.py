# 11729 : 하노이 탑
# https://www.acmicpc.net/problem/11729

def hanoi(N, start, end):
    if N == 1: # 원반이 1개인 경우
        print(start, end)
    
    # 6 - a - b : 기둥 숫자인 1,2,3을 모두 더해서 1, 3번 기둥값을 빼어 보조 기둥으로 사용한다.
    else:
        hanoi(N-1, start, 6-start-end) # 1단계 : N-1개의 원반을 1 -> 2로 옮긴다.
        print(start, end) # 가장 큰 원판을 3번 기둥으로 옮긴다.
        hanoi(N-1, 6-start-end, end) # N-1개의 원반을 2-> 3으로 옮긴다.

N = int(input())

print(2**N - 1) # 하노이 탑의 총 이동 횟수
hanoi(N, 1, 3) # 1번에 있는 N개의 탑을 모두 3번으로 옮기는 작업