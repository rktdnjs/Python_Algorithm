# 1874 : 스택 수열
# https://www.acmicpc.net/problem/1874

import sys

input = sys.stdin.readline
stack = []
operators = []
count = 1
possible = True

N = int(input())

for i in range(N):
    number = int(input())
    # 스택에 push 하는 순서는 반드시 오름차순을 지킨다.
    # 입력받은 숫자를 수열로 만들어주기 위해서는 해당 숫자까지 push한 다음 pop을 해주어야 한다.

    # 아래 구문은 count에 의해서 제어가 된다.
    # 예를 들어 4까지 넣고나서 다음에 3을 입력받았을 경우 count = 4이기 때문에 다시 push를 진행하지 않고 바로 스택에서 pop 절차로 진행된다.
    while count <= number : # 입력받은 숫자까지 push를 실행함
        stack.append(count)
        operators.append("+") # push하는 절차를 기록해둔다!
        count += 1
    
    if stack[-1] == number: # number와 push했던 stack에서 pop할 경우에 숫자가 같을 경우 진행시킴!
        stack.pop()
        operators.append("-")
    else : # 만약 pop하고자 하는 숫자가 현재 stack의 최상단에 없을경우 만들고자 하는 수열은 만들 수 없다
        possible = False

if possible == True:
    for i in operators:
        print(i)
else:
    print("NO")
    