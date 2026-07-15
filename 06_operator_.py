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
