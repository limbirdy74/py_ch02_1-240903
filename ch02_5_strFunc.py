str = "aaabbbbbkk"
print(str.count("k"))  # 해당문자열이 몇 번 나왔다(출현빈도)
print(str.count("bb"))
print("-".join("korea"))  # 해당문자 사이에 삽입됨 k-o-r-e-a

str3 = ["k","o","r","e","a"]
str4 = "".join(str3)  # 여러개의 문자열을 한개로 합칠때
print(str4)

str5 = "Python is the best choice"
print( str5.find("t"))  # 처음 출현하는 위치(인덱스)를 반환한다. 없는 것을 찾으면 -1 반환한다
print( str5.find("is"))

print(str5.upper())  # 대문자로 변경
print(str5.lower())  # 소문자로 변경

str6 = "  맑음    "
print(len(str6))
print(len(str6.strip()))  # strip() 공백제거 크롤링시 많이 딸려옴
print(len(str6.lstrip()))  # 왼쪽공백제거
print(str6.rstrip())  # 오른쪽공백제거

str5 = "Python is the best choice"
str7 = str5.replace("Python", "JAVA")  # old new 는 파이썬이 아니라 파이참에 도움기능
print(str7)

str8 = str5.split()
print(str8)
print(" ".join(str8))
str9 = "a,b,c,d"
str10 = str9.split(",")
print(str10)
print("/".join(str10))