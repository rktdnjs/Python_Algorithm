# 2292 : 벌집
# 개수가 1 - 6 - 12 - 18 - 24 개 이러한 순서로 증가한다
# 해당 규칙을 이용하여 6의 배수를 카운트로 사용해서, 횟수를 측정해보자

Number = int(input()) # 어디 번호까지 이동할 것인지

rooms = 1 # 지나가는 방의 개수는 일단 초기값 1부터 시작
cnt = 1 # 카운트도 또한 6의 배수, 1부터 시작
while Number > rooms :
    rooms += 6 * cnt  # 벌집이 6의 배수로 증가
    cnt += 1  # 반복문을 반복하는 횟수
print(cnt)

"""
입력으로 주어진 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나는지 출력한다.
"""