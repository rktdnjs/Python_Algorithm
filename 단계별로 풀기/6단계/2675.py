"""
문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 
즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. 
S에는 QR Code "alphanumeric" 문자만 들어있다.

QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.
"""

# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다.
# 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. 
# S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 

N = int(input()) # 테스트 케이스의 개수

for i in range(N): # N번 시행
    A, B = input().split() # 반복 횟수와 문자열을 공백을 기준으로 구분하여 받음

    for j in B: # 입력받은 문자열을 기준으로 반복문 시행, for 변수 in iterable 구조
        print(j*int(A), end='') # 문자열의 각 문자를 분리해서 변수(j)에 선언하여 사용한다.
    print()