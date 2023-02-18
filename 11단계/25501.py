# 25501 : 재귀의 귀재
# https://www.acmicpc.net/problem/25501

import sys

def recursion(s, l, r, count): # (문자열, 비교할 지점1, 비교할 지점2) 끝과 끝에서부터 비교를 시작하다 위치가 엇갈리는 순간 비교 종료.
    count += 1
    if l >= r: 
        print(1, count)
        # return 1, global count # 팰린드롬 수라면, 1을 출력
    elif s[l] != s[r]: 
        print(0, count)
        # return 0, global count # 팰린드롬 수가 아니라면, 0을 출력
    else: 
        return recursion(s, l+1, r-1, count) # 비교 지점을 1칸씩 옮김
    

def isPalindrome(s, count):
    count = 0
    return recursion(s, 0, len(s)-1, count)

count = 0 # 전역 변수 사용하려다가 그냥 잘 안되서 인자를 하나 더 넘겨서 사용하는 것으로 고려하였음

N = int(sys.stdin.readline().strip())

for i in range(0, N):
    isPalindrome(sys.stdin.readline().strip(), count)