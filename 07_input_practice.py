# 실습 1
name = input("이름: ")
print(f"안녕하세요{name}님!")     # 안녕하세요(이름)님!
print("안녕하세요"+ name + "님!") # 안녕하세요(이름)님!

# 실습 2
birth_year = int(input("태어난 연도를 입력하세요: "))
print("나이", 2026 - birth_year + 1, "살")

# 실습 3
nation = input("국적을 입력하세요: ")
city = input("도시를 입력하세요: ")
print(nation, "의", city, "에 거주하시는군요!")

# 실습 4
num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("두 번째 숫자를 입력하세요: "))
print("합", num1 + num2)
print("차", num1 - num2)
print("곱", num1 * num2)

# 실습 5
temp = 67
print("80 초과?", temp > 80)    # False
print("0 이상?", temp >= 0)     # True


# 실습 6
score1 = int(input("첫 번째 점수를 입력하세요: "))
score2 = int(input("두 번째 점수를 입력하세요: "))
score3 = int(input("세 번째 점수를 입력하세요: "))

average = (score1 + score2 + score3) / 3
print("평균 점수:", average)
print("60 이상?", average >= 60)





