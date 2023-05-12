# 10951 : A+B - 4

while True:
    try:
        A, B = map(int, input().split())
        print(A + B)
    except:
        break # 아무것도 치지 않았을 경우 while문 종료

# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# EOF : End of file의 약자, 텍스트 파일의 끝임을 알리기 위한 문자 값
# 출력이 완료되고 아무입력도 없을 때 빠져나와야 하므로 except에 EOF 에러를 적어서
# 에러시 break하는 식으로 구현해야 함