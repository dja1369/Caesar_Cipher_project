#소수 체크
#소수란 N 이 1과 N으로만 나누어 지는것을 의미함.
#숫자 입력받기
n = int(input("확인할 숫자를 입력하세요:"))

#소수 판별을 위한 함수 작성
def prime_checker(number):
    #판별용 인자 선언
    is_Prime = True
    #반복문을 이용하여 2부터 N-1값 까지 입력 받고 나누기를 하였을때 나머지가 나오는지 확인
    for num in range (2,number):
        #만약 나머지가 나온다면 이는 소수가 아님
       if (number % num ==0):
           is_Prime = False
        #만약 나머지가 0이 하나도 나오지 않는다면 이는 소수임.
    if(is_Prime == True):
        print(f"{number}는 소수 입니다.")
    else:
        print(f"{number}는 소수가 아닙니다.")
#함수 호출 및 위에서 입력받은 N값을 넣어줌
prime_checker(number = n )

