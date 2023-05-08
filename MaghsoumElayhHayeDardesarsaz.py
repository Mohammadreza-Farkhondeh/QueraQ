n = int(input())
list = []
i = 1
for i in range (1, n+1):
    for j in range (1, int(i/2)+1):
        if i % j == 0:
            list.append(j)
    list.append(i)
print(len(list), sum(list))