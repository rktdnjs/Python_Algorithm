"""
외운 단어가 주어졌을 때, 
이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.
"""

dial_list = ['ABC', 'DEF', 'GHI', 'JKL',  'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()

time = 0
for target in dial_list : # 다이얼 리스트들의 목록에 대해서 반복문 진행
    for alphabet in target : # 이 때 각 다이얼 리스트를 알파벳 철자단위로 반복문 진행
        for search in word : # 입력받은 단어들도 알파벳 철자단위로 반복문 진행
            if search == alphabet : # 만약에 우리가 입력한 알파벳과 해당 다이얼 위치의 알파벳이 일치할경우
                time += dial_list.index(target) + 3 # 다이얼 인덱스에 해당하는 수 + 3을 계속해서 시간에 축적

print(time) # 최종적으로 시간을 출력하며 마무리!