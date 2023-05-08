T = int(input())
listT = []
for t in range (1, T+1):
    values = input().split()
    listT.append(values)
#print((listT[0])[0])
for V in listT:
    n, m, a, b = V
    i = (int(m) + 1) - (int(b))
    j = (int(n) + 1) - (int(a))
    print(i * j)