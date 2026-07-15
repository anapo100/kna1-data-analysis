# # 변수 선언 방법
# # 변수이름 = 값
# # 오른쪽 값을 왼쪽 이름에 "저장"하라는 코드
# temp = 36           # 숫자로 저장하고 싶다면 따옴표 금지
# name = "센서 A"     # 글자는 무조건 따옴표로 감싸기

# print(temp)     # 36
# print("temp")   # temp
# # = 은 "같다"가 아니라 "저장"하는 것
# # 비교는 == 사용


# print("====변수 사용 활용 ====")

# x = 5
# x = x +5 # 변수를 "재할당"할 떄 변수 기존 자시느이 값을 활용할 수 있음

# print(x) # 10

# # y = y + 5 # syntax error: variable 'y' referenced before assignment

# print("==== 재할당 ====")

# print("재할당하기전 temp:", temp)
# temp = 15 # 위에서 할당했던 36이라는 값을 15로 재할당mp
# Temp = 15 # temp와 다른 변수로 동작
# print("temp:", temp, "Temp:", Temp) # temp: 15 Temp: 15

# # 재할당은 지금가지 실행된 코드 중 가장 마지막으로 저장된 값이 불려옴

# score = 10
# score = 20
# score = 30
# score = 40

# print("==== 값 복사 ====")

# a = 10
# b = a
# a = 100

# print(b)

# print("==== 여러 변수 한 번에 선언 및 할당 ====")

# width, height = 10, 20
# print("width:", width, "height:", height)

# print("====주석을 변수 설명====")

# temp = 25 # 온도(섭씨)
# count = 3 # 센서 개수


# 실습 1
# temp = 25
# print(temp)
# name = "센서 A"
# print(name)

# 실습 2
# temp = 30
# print(temp)
# tempurature = 25
# print(tempurature)


# 실습 3
# my_number = 13
# print(my_number)
# mood = "happy"
# print(mood)

# 실습 4
# age = 26
# score = 92
# label1 = "나이"
# label2 = "점수"
# print(label1)
# print(age)
# print(score)

# 실습 5
# x=10
# print(x)  # 10
# x = x + 5
# print(x)  # 15
# x = x * 2
# print(x)  # 30

# 실습 6
# a = 100
# b = a
# a = 999
# print(a)  # 999
# print(b)  # 100

# 실습 7
# # print(temp) # NameError: name 'temp' is not defined
# temp = 25
# print(temp) # 25
# score = 90
# # print(Score) # NameError: name 'Score' is not defined
# print(score) # 90


# 실습 8
# temp = 25 # 온도(섭씨)
# count = 3 # 센서 개수
# # temp = 100
# print(temp) # 25

# 실습 9
# x = 5
# x = 10
# x = x + 1 # 10 + 1
# print(x) # 11


# 실습 10
# name = "이하일"
# age = 26
# city = "포항"
# print("이름:", name)
# print("나이:", age)
# print("도시:", city)
# # 이름: 이하일
# # 나이: 26
# # 도시: 포항

# 실습 11
# a = 25
# b = 3
# # 잘못된 변수 이름
# device_temp = 25
# sensor_count = 3
# print("설비 온도:", device_temp)
# print("센서 카운트:", sensor_count)
# # 설비 온도: 25
# # 센서 카운트: 3

# 실습 12
# x,y,z = 1,2,3
# print(x,y,z) # 1 2 3
# width, height = 4, 3
# print(width, height) # 4 3
# a, b, c = 10, 20, 30  # ValueError: not enough values to unpack (expected 3, got 2)


