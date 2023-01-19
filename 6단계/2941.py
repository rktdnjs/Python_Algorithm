"""
첫째 줄에 최대 100글자의 단어가 주어진다. 알파벳 소문자와 '-', '='로만 이루어져 있다.
단어는 크로아티아 알파벳으로 이루어져 있다. 문제 설명의 표에 나와있는 알파벳은 변경된 형태로 입력된다.
"""

croatia_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
for i in croatia_list: # 크로아티아 알파벳에 대해서 단어를 수정
    word = word.replace(i, 'a') # replace함수, 문자열을 변경!
print(len(word))