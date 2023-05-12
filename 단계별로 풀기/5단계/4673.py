"""
10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램
33 -> 33 + 3 + 3 = 39 이때 33은 39의 생성자.
10000아래의 수 중 생성자를 모두 빼고나면 셀프넘버가 남을것...!
"""

numbers = list(range(1, 10001)) # 1~10000 숫자들 리스트

remove_list = [] # 삭제할 숫자들의 리스트

for num in numbers : # numbers의 개수만큼 반복문 실행, 이때 num은 numbers안의 자료 하나하나
    for number in str(num): # 문자열에 대해서 for문을 실행하면 분리가 된다.
        num += int(number) # 이 분리가 된 숫자들에 대해서 정수로 바꾸어 전부 더함, 생성자를 의미함
    if num <= 10000: # 만약에 이렇게 해서 나온 숫자가 10000이하면 생성자 리스트에 추가함
        remove_list.append(num) # 생성자 리스트를 모두 모아 한꺼번에 뺀다

for remover in set(remove_list) : # 생성자 리스트를 만드는데 중복이 있을 수 있으므로 set을 통해서 중복을 싸그리 제거!
    numbers.remove(remover) # 중복이 제거된 생성자 리스트를 이용해 numbers리스트에서 해당 수들을 제거

for self_num in numbers : # 그러고 나면 이제 셀프 넘버만 덩그러니 남음!!
    print(self_num)
