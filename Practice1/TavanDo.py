n = int(input())
listx = []
for i in range(0,36):
    x = 2 ** i
    while x > n:
        listx.append(x)
        break
print(min(listx))