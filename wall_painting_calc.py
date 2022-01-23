#벽에 페인트를 칠하기 위해 얼마나 사야하는지 계산해주는 프로그램
#함수 선언
def paint_calc(height, width, coverage):
    #페인트 캔의 필요한 갯수를 구하기 위하여 수식 입력
    number_cans = (height * width)  / coverage
    #소수점 단위로 캔을 팔지 않음
    print(f"벽을 칠하는데 필요한 캔은 {number_cans}개 필요합니다.")
    #소수점 단위를 반올림 하여 출력
    print(f"구매하여야 하는 캔의 갯수는: {round(number_cans)}개 입니다.")

#칠해야 하는 벽의 세로 가로 길이 및 적용범위 입력
t_height = int(input("벽의 세로 길이: "))
t_width = int(input("벽의 가로 길이: "))
coverage = 5
#함수에 파라미터 입력하여 출력.
paint_calc(t_height,t_width,coverage)