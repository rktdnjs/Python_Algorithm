# 자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
# 첫째 줄부터 N번째 줄 까지 차례대로 출력한다.

Input = int(input())

for i in reversed(range(Input)):
    print(i + 1)

# reversed를 사용하면 리스트의 원소를 거꾸로 뒤집어서 이를 반환함
# range()는 파라미터 start, step은 생략 가능하며 생략할 시 0, 1로 주어진다.
# range([start] stop [step])의 형태로 구성됨
# 만약 step을 -1로 주게되면, 거꾸로 출력됨