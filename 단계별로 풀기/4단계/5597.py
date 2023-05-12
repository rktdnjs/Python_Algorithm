"""
입력은 총 28줄로 각 제출자(학생)의 출석번호 n(1 ≤ n ≤ 30)가 한 줄에 하나씩 주어진다. 
출석번호에 중복은 없다.
출력은 2줄이다. 1번째 줄엔 제출하지 않은 학생의 출석번호 중 가장 작은 것을 출력하고, 
2번째 줄에선 그 다음 출석번호를 출력한다.
"""

# 리스트를 항목 for 항목 in 반복 가능한 객체 의 형태로 생성해줄 수 있다!
students = [i for i in range(1, 31)]
for i in range(28):
    students.remove(int(input()))

print(min(students))
print(max(students))