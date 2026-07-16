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