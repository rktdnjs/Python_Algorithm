exam_num = int(input()) # 몇 개의 시험을 봤는가?
M = list(map(int, input().split())) # 스페이스바를 기준으로 나눠서 값을 받음
Max_score = max(M) # max함수를 이용해서 M리스트에서 최대값을 찾아옴!!!

for i in range(exam_num): # 시험개수 만큼 반복함
    M[i] = M[i]/Max_score*100 # 시험점수 리스트의 점수들을 최고점수로 나눈다음 100을 곱해서 조작함(세준아!!!!)
print("%.2f" %(sum(M)/ exam_num)) # 새롭게 구한 시험점수들의 총합의 평균을 구한다.
# 이 때 소수 2번째자리까지 출력하도록 함