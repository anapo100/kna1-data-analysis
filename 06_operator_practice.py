# 실습 1
a = 10
b = 3

print(a+b) # 13
print(a-b) # 7
print(a*b) # 30
print(a/b) # 3.3333333333333335
print(a//b) # 3
print(a%b) # 1
print(a**b) # 1000

# 실습 2
c = 10
d = 5
e = 2
print((c+d+e)/3) # 5.666666666666667
slide = 8
print(slide**2) # 64

print(c*d*e) # 100

# 실습 3
a = 10
b = 10
c = "10"
d = "100"
e = "a"

print(a == b) # True
print(a != c) # True
print(c > d) # False
print(c < d) # True
print(e >= c) # False
print(c >= e) # True

# str 비교는 (유니 코드 순서) 순으로 비교됨

# 실습 4
temp = 85
temp_ok = temp >= 60 and temp <= 90
pressur = 5
pressure_ok = pressur <= 7 and pressur >= 3
all_ok = temp_ok and pressure_ok

print(f"온도 정상 {temp_ok}, 압력 정상 {pressure_ok} 모두 정상 {all_ok}")
# 온도 정상 True, 압력 정상 True 모두 정상 True

# 실습 5
stock = 100
stock += 50
print(stock) # 150
stock -= 30
print(stock) # 120
stock += 5
print(stock) # 125

# 실습 6
total = 500
error = 23
error_rate = error / total * 100
run = 21
total_time = 24
run_rate = run / total_time * 100
print(f"불량률 {error_rate}%, 가동률 {run_rate}%")
# 불량률 4.6%, 가동률 87.5%

# 실습 7
run_time = 500
run_hour = run_time / 60
run_minute = run_time % 60
print(f"{run_hour}시간 {run_minute}분")
# 8시간 20분