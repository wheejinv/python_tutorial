# Chapter 03-1 숫자형
# 파이썬 지원 자료형
"""
int: 정수
float: 실수
complex: 복소수
bool: 불린
str: 문자열(시퀀스)
list: 리스트(시퀀스)
tuple: 튜플(시퀀스)
set: 집합
dict: 사
"""

# 데이터 타입
str1 = "python"
str2 = "Anaconda"
list = [str1, str2]
dict = {
	"name": "Test",
	"vesrion": 2.0
}
tuple = (3, 5, 7)
set = {7, 8, 9}

print(type(str1))
print(type(list))
print(type(dict))
print(type(tuple))
print(type(set))

'''
숫자형 연산자
//: 몫
pow(x, y) === x ** y
'''

i = 77
f = 0.9999
print(i + f)  # 77.9999 (실수형으로 형변환)

# 형 변환
print(float(6))  # 정수6.0 (정수 -> 실)
print(float(False))  # 0.0

x, y = divmod(100, 8)  # 100을 8로 나누고 몫과 나머지를 할당
print(x, y)  # 12 4

import math

print(math.pi)  # 3.141592653589793
print(math.ceil(5.1))  # 6
