# Print 사용법

# separator 옵션 사용
print('010', '7777', '7777', sep='-')  # 010-7777-7777
print('NDDC', 'Meta', 'whee', sep=" ")  # NDDC Meta whee

# end 옵션 사용
print('Welcome To', end=' Web')
print(' Python')  # Welcome To Web Python

# format 사용(d: 3, s: 'python', f: 3.14)
print('%s %s' % ('one', 'two'))  # one two
print('{} {}'.format('one', 'two'))  # one two
print('{1} {0}'.format('one', 'two'))  # two one

print('%10s' % ('nice',))  # nice
print('{:>10}'.format('nice'))  # 위와 결과 같음.

print('%-10s' % ('nice',))  # nice      (space)
print('{:<10}'.format('nice'))  # 위와 결과 같음.

print('{:_<10}'.format('nice'))  # nice______
print('{:^10}'.format('nice'))  # nice   (문자열 중간으로)

print('%.5s' % ('pythonstudy'))  # pytho
print('{:.5}'.format('pythonstudy'))  # pytho (절삭)
print('{:10.5}'.format('pythonstudy'))  # pytho     (space), 공간은 10개가 있고

# %d
print('%d %d' % (1, 2))  # 1 2
print('{} {}'.format(1, 2))  # 1 2

print('%4d' % (42,))  # 42
print('{:4d}'.format(42))  # 42

# %f
print('%f' % (3.141592653589793,))  # 3.141593
print('{:f}'.format(3.141592653589793))  # 3.141593

print('%06.2f' % (3.141592653589793,))  # 003.14
print('{:06.2f}'.format(3.141592653589793))  # 003.14
