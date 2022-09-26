prices = int(input())
category = int(input())
result = 0

for i in range(0, category) :
    item, price = input().split()
    
    result += int(item)*int(price)

if(prices == result):
    print("Yes")
else:
    print("No")