# 파이썬

# 기본 선언
m = n = 700

print(n)  # 700
print(type(n))  # <class 'int'>

# Object References
# 타입에 맞는 오브젝트 생성
print(id(n))  # 4347363792
print(id(m))  # 4347363792
m = 300
print(id(m))  # 4564092032 (따로 대입을 해야 id가 갈림)
