x = (input())
while ((int(x)) % 10) != (int(x)):
    x = str(sum(list(map(int,x))))
print(x)