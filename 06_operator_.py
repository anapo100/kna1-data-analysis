# 산술 연산자
# + - * / % // **

print(3+5) # 8
print(10-4) # 6
print(4*5) # 20
print(9/3) # 3.0
print(10%3) # 1
print(10//3) # 3
print(2**3) # 8

# 연산 우선순위는 괄호 사용
# 우선순위**(거듭제곱) > *(곱하기) /(나누기) //(몫) %(나머지) > +(더하기) -(빼기)

# 복합 할당 연산자
# +=, -=, *=

result = 3*5
print(result) # 15

# result = result + 3  == result += 3

result += 10
print(result) # 25

# result = result - 5 == result -= 5
result -= 5
print(result) # 20

# result = result * 3  == result *= 3
result *= 3
print(result) # 60

# result = result / 2 == result /= 2
result /= 2
print(result) # 30.0


# 문자열 연산
print("안녕" + "하세요") # 안녕하세요

# 만약 안녕과 하세요 사이에 공백을 1개 넣고싶다면?
# 방법1
print("안녕", "하세요") # 안녕 하세요
# 방법2
print("안녕 "+"하세요") # 안녕 하세요
# 방법3
print("안녕" + " " + "하세요") # 안녕 하세요

print("안녕"*5) # 안녕안녕안녕안녕안녕

# 비교 연산자
# <(미만) >(초과) <=(이하) >=(이상) ==(같다) !=(다르다)
# 비교 연산자는 무조건 True or False (boolean) 결과
print(7 < 16) # True
print(7 > 16) # False
print(7 <= 7) # True
print(7 >= 7) # True
print(7 == 7) # True
print(7 != 7) # False

# 비교 연산자는 문자열 비교도 가능
print("hello" == "hello") # True
print("정상" == "정상") # True

# 비교 연산자 사용 문자열 비교시 주의사항

# 1. 대소문자 구분
print("hello" == "Hello") # False

# 2. 공백도 문자로 취급
print("정상" == "정상 ") # False

# 부정연산자 != (not)
print("hello" != "hello") # False
print("hello" != "hello ") # True
print("hello" != "Hello") # True

# 변술 비교 연산자 사용 
num1 = 123
num2 = 456

print(num1 >= num2) # False
print(num1 >= "num2") # TypeError: '>=' not supported between instances of 'int' and 'str'

# 논리 연산자
# and / or / not
# and : 모두 True 일때만 True
print(5 == 5 and 7 == 7) # True
print(5 == 7 and 7 == 7) # False
print(5 == 5 and 7 != 7) # False

# or : 하나라도 True면 True
print(5 == 5 or 7 == 7) # True
print(5 == 7 or 7 == 7) # True
print(5 == 7 or 7 != 7) # False

# not : True를 False로, False를 True로
print(not True) # False
print(not 5 == 5) # False