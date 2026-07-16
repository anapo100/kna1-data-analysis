# input - 사용자 입력

input("이름: ") # 입력해야 하는 값을 명시 가능

# 1. 값을 여러개 받아야 할 때 필요한 만큼 input() 함수 사용
input("나이: ")
input("직업: ")

# 2. 가이드 문구에 규칙과 함께 입력 받기
input("나이, 직업을 입력하세요.  예: 20, 학생: ")

# input 함수 활용 방법
name = input("이름: ")
age = input("나이: ")

print("입력 받은 이름: ", name, "입니다.")
print("입력 받은 나이: ", age, "살 입니다.")

# input으로 받은 값은 항상 문자열(str) 로 저장됨

# 사용자에게 입력받은 값을 한 번에 출력하기
print("이름", name, "나이", age, "살")

# int() 문자열을 int(정수형)으로 변환

age = int(input("나이: ")) # 문자열을 정수형으로 변환
type(age) # <class 'int'>

# float() 문자열을 float(실수형)으로 변환
print(float(3.14))   # 3.14
print(float("3.14")) # 3.14
print(float(12))    # 12.0

# 사용자 입력값을 float으로 변환
tall = float(input("키: "))
print("tall:", tall,"tall의 자료형", type(tall))  # <class 'float'>

# str() 정수형, 실수형을 문자열로 변환
year = int(input("태어난 연도를 입력하세요: "))
print("당신의 나이는 "+ str(2026 - year + 1) + "세 입니다.")

