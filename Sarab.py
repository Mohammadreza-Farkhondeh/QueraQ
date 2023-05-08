t = int(input())
listr= []
for t in range (1,t+1):
    x, y = input().split()
    x, y = int(x), int(y)
    if x==y :
        if x % 2 == 0:
            listr.append(2*x)
        else:
            listr.append((2*x)-1)
    elif int(x)+2 == int(y) or int(x)==int(y)+2:
        if x % 2 == 0:
            listr.append((2*x)-2)
        else:
            listr.append((2*x)-3)
    else:
        listr.append(-1)
for i in range (0, t):
    print(listr[i])