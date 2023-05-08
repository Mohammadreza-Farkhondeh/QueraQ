a = int(input())
b = int(input())
m = (a // 100) + (((a % 100) // 10) * 10) + ((a % 10) * 100)
n = (b // 100) + (((b % 100) // 10) * 10) + ((b % 10) * 100)
if m > n:
    print(b,'<',a)

elif n > m:
    print(a,'<',b)
else:
    print(a,'=',b)