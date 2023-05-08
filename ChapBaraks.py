n = int(input())
listn = []
while n != 0:
    listn.append(n)
    n = int(input())
for i in range(1,len(listn)):
    print(listn[-i])
print(listn[0])