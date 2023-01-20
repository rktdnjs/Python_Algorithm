# 4344 : 평균은 넘겠지

N = int(input()) # 테스트 케이스 개수를 입력받음

for i in range(N): # 테스트 케이스만큼 반복
    scores = list(map(int, input().split())) # 스페이스바를 기준으로 나눠서 값을 받음, int데이터를 지닌 리스트로 변환
    avg = sum(scores[1:])/scores[0] 
    # 점수 리스트에서 '1번째 ~ 끝까지 슬라이싱(점수 목록)'을 모두 합함
    # 점수의 모든 합을 점수 '리스트 0번째 요소(학생 수)'로 나누어 주면, 평균을 얻음!!
    
    count = 0 # 평균을 구하는데, 이때 평균을 넘는 학생을 카운트 할 것
    for i in scores[1:] : #점수 리스트의 1번째 ~ 끝까지 요소에 대해서 진행
        if i > avg: # 특정 학생의 점수가 평균보다 높다면, count + 1을 계산. 카운팅!
            count += 1
    
    rate = (count/scores[0]) * 100 # 총 카운트 횟수를 학생수(점수 리스트0번째)로 나누어 백분율을 구한다.

    print('%.3f'%rate + '%') # 구한 비율을 소수점 3번째 까지 실수형태로 나타낸다.

"""
https://www.acmicpc.net/problem/4344

첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고,
이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
"""