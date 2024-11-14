# string test
str1 = "Korea"
print(str1[0] + "\t" + str1[1])
print(str1[2])  # 인덱싱
s1 = str1[4]
str2 = "안녕하세요 반가워요"
print(str2[9])
str3 = "Life is too Short"
print(len(str3)) # 길이 함수
print(str3[16])
print(str3[-2])  # 뒤 부터 카운트
str4 = "20240903sunny"
print(str4[4:8])  # 마지막은 포함되지 않는다
print(str3[8:11])  #
str5 = str3[8:17]  # 끝은 생략가능 (문자를 끝까지 슬라이싱하는 경우)
str6 = str3[8:]
str7 = str3[:7]  # 첫 글자부터 슬라이싱을 시작할 때는 시작인덱스 생략가능 str3[0:7]
print(str5, str6, str7)