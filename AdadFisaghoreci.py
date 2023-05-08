a = input()
b = input()
c = input()
a = int(a)
b = int(b)
c = int(c)
if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2:
    print('YES')
else:
    print('NO')
