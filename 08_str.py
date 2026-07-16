# """ """ - 여러줄 문자열

notice = """ 설비 점검 안내
1. 전원 확인
2. 센서 확인"""
# 직접 작성한 줄바뿜이 반영되어 여러 줄로 출력됨
print(notice)
# """ """ (삼중 따온표를 사용 시 그 내부의 모든 줄바꿈이 반영되 출력)"


# 이스케이프 문자
# \n : 줄바꿈, \t : 탭 \\ : 백슬래시, \' : 작은 따옴표, \" : 큰 따옴표

# notice  이스케이프 사용해서 개선
notice  = "설비 점검 안내\n1. 전원 확인\n2. 센서 확인"
print(notice)

tap = "이름\t상태"
print(tap)
print("이름 상태")

bacjslash = "이름 \\ 상태"
print(bacjslash)

quotes = 'It\'s me'
print(quotes)

# 빈 문자열과 공백 문자열의 차이
# "" 따옴표로 감싸졌지만 아무것도 작성되지 않았다면 빈 문자열
# 빈 문자열은 글자 수 0, 길이 0

# "" 따옴표 안에 공백(스페이스 바)이 있는 경우는 공백 문자열
# 공백(스페이스 바)의 수 만큼 글자가 있고, 길이가 세어짐
# 빈 문자열과 공백 문자열은 컴퓨터에게 다른 값으로 인식됨

# 실습 예제
pump = "PUMP_A"
state = "정상"
run_time = 1200
maintenance_date = "2026-07-16"
card = "설비:"+ pump + "\n상태:" + state + "\n가동:" + str(run_time) + "\n점검:" + maintenance_date

print(card)



# 인덱싱 - 위치 번호로 글자를 하나 꺼내기
# 문자열 [인덱스 번호]   문자열 첫 글자 인덱스는 0이다.

word = "PYTHON"
print(word[0], word[3], word[5])  # P H N

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(alphabet[11], alphabet[4],alphabet[4], alphabet[7], alphabet[0], alphabet[8], alphabet[11]) # LEEHAIL

# 음수 인덱스는 뒤에서 부터 역순으로 숫자가 붙음
# 음수 인덱스는 가장 마지막 글자가 -1 부터 시작됨

# 슬라이싱
# 문자열[시작인덱스:끝인덱스]
# 시작인덱스 글자는 포함, 끝 인덱스 글자는 제외

print(word[3:5]) # HO
print(word[3:6]) # HON

# 슬라이싱 - start 생략
# 처음부터 특정 인덱스까지 구간을 뽑아내고 싶을 때 사용
print(word[:4]) # print(word[0:4])와 동일한 출력 # PYTH

# 슬라이싱- end 생략
# 특정 인덱스 부터 끝까지 구간을 뽑아내고 싶을 때 사용
print(word[2:6]) # print(word[2:6])와 동일한 출력 # THON

# 슬라이싱 - 전체 생략
print(word[:]) # print(word[0:6])와 동일한 출력 # PYTHON

# 슬라이싱 - 음수 인덱스 사용
print(word[-3:]) # print(word[3:6])와 동일한 출력 # HON
print(word[:-1]) # print(word[0:5])와 동일한 출력 # PYTHO

# step으로 건너뛰기
print(word[::2]) # PTO
print(word[::-1]) # NOHTYP

# 실습 1
word = "temp_sensor"
print(word[0:4]) # temp

# 실습 2
word = "temp_sensor"
print(word[5:]) # sensor

# 실습 3
word = "sensor_01"
print(word[-2:]) # 01

# 실습 4
word = "PYTHON"
print(word[::2]) # PTO


# 실습 5
word = "PYTHON"
print(word[::-1]) # NOHTYP


# len() 함수 - 문자열 길이 반환
# len(문자열)

print(len("Hello World!")) # 12
print(len("")) # 0

var = "모두 화이팅!"
print(len(var)) # 6

# len()은 int를 반환하므로 연산이 가능

# 음수 인덱스를 사용하지 않고 마지막 인덱스 문자를 뽑고 싶을 때
print("abc"[len("abc") - 1]) # c

# 실습 1
phone = "01012345678"
print(len(phone)) # 11



# in 특정 문자가 문자열에 포함되었는지 확인
# 결과는 True, False로 반환됨
# 찾을 문자열 in 문자열
print("고장" in "설비 고장 발생") # True
print("정상" in "설비 고장 발생") # False


# not in - in과 정 반대 동작
print("고장" not in "설비 고장 발생") # False
print("정상" not in "설비 고장 발생") # True



# .count() - 특정 문자가 문자열에 몇 번 포함되었는지 확인
# 문자열.count(찾을 문자열)
print("banana".count("a")) # 3
print("010-1234-1234".count("-")) # 2
print("example@example.com".count("@")) # 1

# 실습 1
print('a,b,c,d'.count(',')) # 3

# find() - 특정 문자가 문자열에 포함되어 있는지 확인하고,
#          포함되어 있다면 처음 나오는 위치를 반환
#          포함되어 있지 않다면 -1을 반환
email = "example@example.com"
at = email.find("@")
print(at) # 7


