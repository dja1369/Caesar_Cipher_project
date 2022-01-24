# 카이사르 암호기 제작
# 알파벳의 범위중 z가 먼저 나오면 인덱스가 초과되기에 알파벳을 한번더 복사하여 범위 해결
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
type = input("encode 는 암호화 , decode 는 해독화 입니다 둘중하나를 선택하여 주세요:\n").lower()
# 텍스트를 입력받고 대소문자의 구분을 없애기 위해 전부 소문자로 변환하여 저장
text = input("텍스트를 입력하세요(영어로) :\n").lower()
# 이동할 숫자를 문자열로 입력받고 정수형으로 변환
shift = int(input("넘어갈 숫자를 입력하세요 :\n"))


# 암호화 및 해독 하는 코드 정의
#좀더 간단하게 합쳐본 코드
def Caesar(insert_text, insert_shift, insert_type):
    cipher_text = ""
    if insert_type == "decode":
        insert_shift *= -1
    for char in insert_text:
        position = alphabet.index(char)
        new_position = position + insert_shift
        new_word = alphabet[new_position]
        cipher_text += new_word
    print(f"{insert_text}는 {cipher_text} 입니다.")


Caesar(insert_type=type, insert_text=text, insert_shift=shift)
