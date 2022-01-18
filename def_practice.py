#함수를 호출하면 내용이 변경되지 않고 그대로 출력됨
def greet():
    print("함수 연습1 입니다.")
    print("함수 연습2 입니다.")
    print("함수 연습3 입니다.")
greet()

#함수에 매개변수를 추가하여 내용값을 입력할수 있음.
def greet_02(string1, string2, string3):
    print(f"함수의 내용은 {string1} 입니다.")
    print(f"함수의 내용은 {string2} 입니다.")
    print(f"함수의 내용은 {string3} 입니다.")
greet_02("함수의 내용을 변경할수 있어요", "각각의 내용을 넣어줄수 있어요", " 다채롭게 바뀌었네요.")
#키워드 인자를 사용한다면
greet_02(string1="키",string2="워",string3="드 인자")



