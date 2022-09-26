def bubbleSort(list) :

    length = len(list)

    for i in range(0, length-1) :

        print("")
        print("i :", i)

        for j in range(0, length-1-i) :

            print("j :", j)
            if(list[j] > list[j+1]) : 
                list[j], list[j+1] = list[j+1], list[j]

list = [5,1,4,2,8]
bubbleSort(list)
print(list)

# 큰 숫자가 매 사이클 마다 맨 오른쪽으로 가는 정렬(오름차순)
# 결과 : [1, 2, 4, 5, 8]
# 반복문이 중첩으로 들어갔으므로 이 친구의 Big-O 표기는 O(n^2)이다.