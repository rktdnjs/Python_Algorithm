# 4949 : 균형잡힌 세상
# https://www.acmicpc.net/problem/4949

# import sys 여기서는 얘 쓰면 틀림

# 균형잡힙 문자열 체크용 덱 선언
while True:
    word = input()

    # 종료 조건에 만족 시 반복문 종료
    if word =='.':
        break
        
    word_stack = [] # 문자 하나하나 저장용
    result = True
    
    # 문자 하나하나에 대해서 체크
    for find in word:
        if find == '(' or find == '[':
            word_stack.append(find)

        elif find==')':
            # 스택에 아무것도 없거나 마지막 문자가 대괄호면 조건 불만족
            if len(word_stack) == 0 or word_stack[-1] == '[':
                result = False
                break
            elif word_stack[-1] == '(':
                word_stack.pop()

        elif find==']':
            if len(word_stack) == 0 or word_stack[-1]=='(':
                result = False
                break
            elif word_stack[-1] == '[':
                word_stack.pop()

    # 성공적으로 끝났으면 yes, 아니면 no 출력하고 종료
    if len(word_stack)==0 and result==True:
        print('yes')
    else:
        print('no')