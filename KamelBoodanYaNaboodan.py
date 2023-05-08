n = input()
n = int(n)
listi = []
for i in range(1,n):
    if n % i == 0:
        listi.append(i)
if sum(listi) == n:
    print('YES')
else:
    print('NO')