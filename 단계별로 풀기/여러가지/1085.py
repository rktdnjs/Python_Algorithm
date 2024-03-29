# 1085 : 직사각형에서 탈출
# acmicpc.net/problem/1085
# 전제조건을 보니, 직사각형 안에 있음을 가정하고 진행

x, y, w, h = map(int , input().split()) # 오른쪽 위 꼭짓점 = w, h

print(min(x, y, w-x, h-y))

"""
한수는 지금 (x, y)에 있다. 직사각형은 각 변이 좌표축에 평행하고, 
왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다. 
직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.

첫째 줄에 x, y, w, h가 주어진다.
첫째 줄에 문제의 정답을 출력한다.
"""