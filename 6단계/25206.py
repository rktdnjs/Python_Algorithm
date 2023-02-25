# 25206 : 너의 평점은
# https://www.acmicpc.net/problem/25206
# 과목이름, 학점, 과목평점을 입력받는다.
# 과목이름은 1~50자라는 제한을 가지고 있다.
# 학점은 1.0 2.0 3.0 4.0 중 하나
# 등금은 A+ ~ D0(1.0), F / P(P는 평점 계산에서 제외)

import sys

totalScore = 0 # 등급에 따른 점수 계산용
count = 0 # P인 과목이 있다면 1씩 차감한다.

def scores(score, grade):
    global totalScore 
    global count
    if grade == "A+":
       totalScore += 4.5 * score
       count += score 
    elif grade == "A0":
       totalScore += 4.0 * score
       count += score
    elif grade == "B+":
       totalScore += 3.5 * score
       count += score 
    elif grade == "B0":
       totalScore += 3.0 * score
       count += score 
    elif grade == "C+":
       totalScore += 2.5 * score
       count += score 
    elif grade == "C0":
       totalScore += 2.0 * score
       count += score 
    elif grade == "D+":
       totalScore += 1.5 * score
       count += score
    elif grade == "D0":
       totalScore += 1.0 * score
       count += score
    elif grade == "F":
       totalScore += 0.0 * score
       count += score   
    elif grade == "P":
       pass # 등금이 P인 과목을 전체 과목 평점 계산에서 제외한다.

# 수강한 과목들에 대한 정보를 담기위한 리스트
List = []

for i in range(0, 20): # 20개 과목을 입력받는다.
    tmp = 0 # List에 넣을 임시 tmp 리스트를 만든다. 
    tmp = list(sys.stdin.readline().split())
    tmp[1] = float(tmp[1]) # 학점에 해당하는 부분을 실수로 변환한다.
    List.append(tmp)

# 전부 입력 받고 난 다음...
for i in range(0, 20):
    scores(List[i][1], List[i][2]) # 수강한 과목들의 학점과 등급을 함수의 매개변수로 보낸다.

print(format(totalScore/count, ".6f"))

"""
나는 그냥 일일이 함수로 받아 계산하다보니 코드가 되게 복잡해졌는데,
그냥 딕셔너리를 활용하면 훨씬 간단하게 구현할 수 있다.

[아래 코드 참고!!!]
# 함수를 호출할 때 딕셔너리를 이용하여 대응 요소를 빠르게 찾는다.
def convert_rating_to_score(rating):
    rating_dict = {
        "A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0,
        "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, 
        "F": 0.0
    }
    
    return rating_dict[rating]

# 이렇게 하면 매우 간단히 구현가능하다.
def calculate_grade(record_list):
    total_time, total_score = 0, 0
    
    for record in record_list:
        subject_name, time, rating = record.split()
        
        if rating == "P":
            continue
            
        total_time += float(time)
        
        total_score += convert_rating_to_score(rating=rating) * float(time)
        
    return total_score / total_time
"""