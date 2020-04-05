# Chapter 03-2
# 파있ㄴ 문자형

# 문자열 생성
str1 = "I am Python"
str2 = "Python"
str3 = """How are you?"""

print(type(str1), type(str2), type(str3))
print(len(str1), len(str2), len(str3))

# 빈 문자열
str1_t1 = ''
str2_t2 = str()

# Row String = \ 자체를 신경쓰지 않는다. 앞에 r 붙임.
raw_s1 = r'D:\python\test'

print(raw_s1)

# 멀티라인 입력, 긴 텍스트인 경우 잘라서 보기 좋게 처리하고 싶을 때,
# \ 붙여서 사용하면 보기 좋음.
multi_str = \
	"""
	문자열
	멀티 라인 입력
	테스트
	"""
print(multi_str)

# 문자열 연신
str1 = 'Python'
print(str1 * 3)
print('thon' in str1)
print('Py' not in str1)

# 문자열 함수
# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha 등)
print("Capitalize: ", str1.capitalize())
print("endswith?: ", str1.endswith("s"))
print("join str: ", str1.join(["I'm ", "!"]))
print("replace1: ", str1.replace('thon', ' Good'))
print("replace2: ", str1.replace("are", "was"))
print("split: ", str1.split(' '))  # Type 확인
print("sorted: ", sorted(str1))  # reverse=True
print("reversed1: ", reversed(str1))  # list 형 변환
print("reversed2: ", list(reversed(str1)))

# 슬라이싱 a[start : end : step], step: stride 라고도 하며 몇개씩 끊어서 가져올지를 정한다.
str = 'Nice Python'
print(str[0:3])  # Nic
print(str[5:])  # Python
print(str[:len(str)])
print(str[1:4:2])  # ie, 3번째 인자는
print(str[1:-2])  # ice Pyth
print(str[::2])  # Nc yhn

# 아스키 코드
print(ord('A'))  # 65
print(chr(65))  # A
