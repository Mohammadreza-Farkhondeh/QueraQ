n = input()
n = int(n)
j = 1
if n >= 0:
    if n <= 1:
        print (1)
    else:
        for i in range (1, n+1):
            j = j * i
        print(j)