# 정수형 int: 소수점 없이 딱 떨어지는 수
# 0과 음수도 정수에 포함됨
count = 3
age = 20
tall = 173
temp = -20
zero = 0

# 실수형 float: 딱 떨어지더라도 소수점이 있으면 실수형
tired = 99.9999
height = 17.2

# 문자열 str: 따옴표에 감싸져 있는 모든 값
hello = "안녕하세요~!"
emoji = "❤️"
empty = ""
fake_num = "12345"
fake_num2 = "5.0"

# 불린형 bool: True 또는 False 값을 가짐
ok = True
no = False

print(100 < 5) # False
print(5 == 5) # True

# type(): 자료형을 확인할 수 있다.
print(type(count))    # <class 'int'>
print(type("센서 A")) # <class 'str'>
print(type(True))     # <class 'bool'>
print(type(3 > 2))    # <class 'bool'>


num = 123
fake_num = "123"
str = "문자열"
ok = True

print(num, type(num))         # 123 <class 'int'>
print(fake_num, type(fake_num)) # 123 <class 'str'>
print(str, type(str))         # 문자열 <class 'str'>
print(ok, type(ok))           # True <class 'bool'>

