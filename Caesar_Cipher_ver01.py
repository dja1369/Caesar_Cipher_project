#카이사르 암호기 제작
#알파벳의 범위중 z가 먼저 나오면 인덱스가 초과되기에 알파벳을 한번더 복사하여 범위 해결
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
type = input("encode 는 암호화 , decode 는 해독화 입니다 둘중하나를 선택하여 주세요:\n").lower()
#텍스트를 입력받고 대소문자의 구분을 없애기 위해 전부 소문자로 변환하여 저장
text = input("텍스트를 입력하세요(영어로) :\n").lower()
#이동할 숫자를 문자열로 입력받고 정수형으로 변환
shift = int(input("넘어갈 숫자를 입력하세요 :\n"))
#암호화 하는 코드 정의
def encrypt(C_text,C_shift):
    #변환된 값을 저장할 빈 문자 선언
    cipher_text = ""
    # C_text의 크기만큼 char 이란 변수가 +1이 되면서 반복
    for char in C_text:
        #포지션 이라는 변수에 알파벳의 인덱스(char)의 값을 넣어주고 저장
        position = alphabet.index(char)
        #새로운 뉴_포지션에 포지션에 입력된 인덱스 수 + 변화할 값 을 넣어서 이동 if index(5) + shift(3) = 8
        new_position = position + C_shift
        #뉴_워드에 알파벳[뉴포지션]인덱스에 있는 글자를 넣어줌
        new_word = alphabet[new_position]
        #사이퍼_텍스트 에 뉴텍스트를 넣어주면서 종합함.
        cipher_text += new_word
        #반복하는 변수 char 이 C_text의 크기만큼 반복하며 입력받은 문자를 알파벳이란 리스트에서 찾음
        #Ex) B를 입력받으면 알파벳에서 a>>b로 넘어가며 위치를 찾는다.
        #찾아낸 위치 1에 움직일값을 넣어주어 만약 5를 움직인다 가정하면 1+5 = 6
        #인덱스중 6은 a,b,c,d,e,f,g 중 g가 된다
        #변경된 값은 알파벳[원래값+이동값] 에서 찾아내고 이를 뉴_워드에 넣어준다
        #뉴_워드에 넣어진 새로운값은 암호화_텍스트에 더해서 넣어주어 저장한다
    print(f"암호화된 문자는 {cipher_text} 입니다.")
def decrypt(D_text,D_shift):
    cipher_text = ""
    for char in D_text:
        position = alphabet.index(char)
        new_position = position - D_shift
        new_word = alphabet[new_position]
        cipher_text += new_word
    print(f"해독된 문자는 {cipher_text} 입니다.")

if(type == "encode"):
    encrypt(C_text=text, C_shift=shift)
elif(type == "decode"):
    decrypt(D_text=text, D_shift=shift)