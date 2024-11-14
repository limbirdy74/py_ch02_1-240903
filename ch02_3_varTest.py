# 변수 연습
# 변수는 대부분소문자 로 시작 특수문자 불가능(_ 가능), 숫자가 앞에 올 수 없음

a = 1
avg_sum = 100
korAvg = 70  # 소문자 대문자 혼용 가능 카멜 표기법
koravg = 50  # 대소문자 구별
print(korAvg + koravg)

# 변수를 선언한다 라는 표현사용
#score
# 변수를 100 으로 초기화 되었다. 파이썬 에선 선언하고 초기화 해줘야 한다
score = 100  # '=' 등호기호가 아니라 대입연산자 (오른쪽 값을 왼쪽에 넣어주는 연산자)
print(id(score))  # 변수가 저장된 메모리 번지 주소를 알려줌 쓸 일은 없음
str = "korea"
str2 = str  # 얕은 복사. 복사가 되긴 하지만 값이 복사되어 메모리가 만들어지는 것이 아니라 값이 있는 주소가 복사된다
print(id(str), "\t" , id(str2))
str = "japan"
print(id(str), "\t" , id(str2))
print(str + str2)
print(str , str2)