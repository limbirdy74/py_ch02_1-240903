# 한번에 주석 ctrl + /
# 1. 에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다. 총 금액을 계산한 후 이를 화면에 출력해보세요. (변수사용하기)
mon_inst = 48584
total_mon = 36
air_price = mon_inst * total_mon
print("에어컨의 판매금액은 %d원 입니다" % air_price)
print("%d원" % air_price)
print(f"에어컨의 판매금액은 {air_price:,}원 입니다")
print(f"에어컨의 판매금액은 {mon_inst * total_mon:,}원 입니다")
# 2. letters가 문자열 변수에 저장하고 첫번째와 세번째 문자를 출력하세요.
str2 = "letters"
print(str2[0])
print(str2[2])
# 3. 자동차 번호가 다음과 같을 때 뒤에 4자리 중 앞의 두자리인 22만 출력하세요.
#
#    license_plate = "24가 2210"
license_plate = "24가 2210"
print(license_plate[4:6])
# 4. url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
#
#    url = "http://jbedu.or.kr"
#    실행 예:
#    or.kr
url = "http://jbedu.or.kr"
print(url[-5:])
print(url[13:])
print(url[url.find("o"):])
# 5. 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
#
#   string = 'abcdfe2a354a32a'
#   실행 예:
#   Abcdfe2A354A32A
str3 = 'abcdfe2a354a32a'
str4 = str3.replace("a", "A")
print(str4)
# 6. 화면에 '-'를 80개 출력하세요.
#
# 실행 예:
# --------------------------------------------------------------------------------
print("-"*80)
# 7. 변수에 다음과 같은 문자열이 저장되어 있습니다.
#
#    t1 = 'python'
#    t2 = 'java'
# 변수에 문자열 더하기와 문자열 곱하기를 사용해서 아래와 같이 출력해보세요.
#
# 실행 예:
# python java python java python java python java
t1 = 'python'
t2 = 'java'
print((t1 + " " + t2 +" ") * 4)
# 8. 변수에 다음과 같이 문자열과 정수가 저장되어 있을 때 f-string을 사용해서 다음과 같이 출력해보세요.
#
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
#
# 이름: 김민수 나이: 10
# 이름: 이철희 나이: 13
#
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")
# 9. 문자열의 좌우의 공백이 있을 때 이를 제거해보세요.
#
data = "   삼성전자    "
#
data_trim = data.strip()
print(data_trim)
# 10. 다음과 같은 문자열이 있을 때 이를 대문자 KOREA_FIGHTING로 변경하세요.
#
#    ticker = "korea_fighting"
ticker = "korea_fighting"
ticker_upper = ticker.upper()
print(ticker_upper)
