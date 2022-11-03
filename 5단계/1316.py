# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 
# 각 문자가 연속해서 나타나는 경우만을 말한다.
# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.
# 첫째 줄에 그룹 단어의 개수를 출력한다.

N = int(input()) # 입력받을 단어의 개수를 입력받는다.
cnt = 0

for i in range(N):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            cnt += 1
            break
        elif word[j] in word[j+1:]:
            pass

print(cnt)