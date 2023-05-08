n = int(input())
listx = []
for i in range (1, n+1):
    for j in range (1, n+1):
        listx.append(str(i*j))
        strx = ' '.join(listx)
    print(strx)
    listx = []