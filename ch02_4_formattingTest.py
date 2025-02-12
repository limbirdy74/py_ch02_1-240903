# formatting 연습
num = 7

print("내가 제일 종아하는 숫자는 7입니다.")
print("내가 제일 종아하는 숫자는 %d 입니다." % num)

str = ("대한민국")
print("우리나라는 %s입니다" % str)
# %s   문자열
# %c   문자1개
# %d   정수
# %f   부동소수

num2 = 3.14
print("원주율 : %f입니다" % num2)  # 기본 소수점 6자리까지 찍음
print("원주율 : %0.2f입니다" % num2)  # 소수점 자릿수를 지정가능
print("원주율 : %d입니다" % num2)  # 실수를 정수형 포멧코드로 출력시 소숫점 이하부분은 버림

num3 = 1
num4 = 2
print("내가 좋아하는 숫자는 %d이고, 너는 %d입니다" % (num3, num4))  # 두개 포멧팅 올드한 방법
# f 문자열 포매팅(f string)
name = "홍길동"
score = 88.5
grade = 2
print("학생 이름은 [홍길동]이고, 학년은 [2]학년 이고, 점수는 [88.5]점 입니다")
print("학생 이름은 %s이고, 학년은 %d학년 이고, 점수는 %f점 입니다" % (name, grade, score))

print(f"학생 이름은 {name}이고, 학년은 {grade}학년 이고, 점수는 {score}점 입니다")

num5 = 3.141592
print(f"원주율 :{num5}")
print(f"원주율 :{num5:.2f}")  # 소숫점 자리수 설정
num6 = 10000000
print(f"이번달 수입 : {num6:,}원")  # 1000단위 마다 , 표시
print(f"이번달 수입 : {num6-500000:,}원")  # {} 안에서 연산도 가능. 문자열의 영향을 받지 않음
print(f"이번달 수입 : {num6+num5:,}원")
print(f"내이름의 글자수는 {len(name)}입니다")  # {} 안에서 함수도 사용가능