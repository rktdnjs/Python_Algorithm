def bubbleSort(list) :
    for i in range(0, length-1) :
        for j in range(0, length-1-i) :
            if(list[j] > list[j+1]) : # 만약 현재 i번째 사이클에서  j j+1번째 를 비교하여 j가 크면 위치 변경
                list[j], list[j+1] = list[j+1], list[j]

length = int(input())
list = []
for i in range(0, length):
    list.append(int(input())) # 입력 받은 수를 리스트에 추가!!

bubbleSort(list)

for i in range(0, length):
    print(list[i])