list = list(map(int, input().split()))
OK = False
for i in list:
    for j in list:
        for k in list:
            if i**2+j**2==k**2:
                OK = True
                break
# or i**2+k**2==j**2 or j**2+k**2==i**2
if OK:
    print('Yes')
else:
    print('No')