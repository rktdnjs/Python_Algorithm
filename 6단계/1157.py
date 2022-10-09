"""
알파벳 대소문자로 된 단어가 주어지면, 
이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
단, 대문자와 소문자를 구분하지 않는다.
"""
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다.

word = input().upper() # 대소문자를 구분하지 않기 때문에 그냥 전부 대문자로 변환
alphabet = list(set(word)) # 우선, 이 단어에 무슨 알파벳이 쓰였는지 체크하기 위해 중복 제거한 알파벳 리스트를 생성
# print(alphabet)

count_list = []
for x in alphabet : # 단어에 쓰인 알파벳들을 대상으로 반복문 진행
    count = word.count(x) # 각각의 알파벳이 몇 번 쓰였는가?
    count_list.append(count) # 그 알파벳이 쓰인 만큼 카운트를 세서 추가
    # count함수는 문자열 내부에서 특정 문자 혹은 문자열이 포함 되어 있는지
    # 계산해서 반환해주는 함수이다. .count(x, start, end)
    # 대소문자를 구분하며, start end에 아무것도 넣지 않으면 문자열 처음~끝까지 탐색!
    # 찾는 x의 범위는 start 포함 ~ end 이전까지이다.

if count_list.count(max(count_list)) > 1 : # 만약 제일 많이 쓰인 횟수가 2개 이상일 경우
    print('?')
else :
    max_index = count_list.index(max(count_list)) # 제일 많이 쓰인 수의 위치를 반환함
    print(alphabet[max_index]) # 그 위치에 해당하는 알파벳을 출력해준다.
    