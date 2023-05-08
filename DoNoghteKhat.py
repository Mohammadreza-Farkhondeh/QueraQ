listd = input()
listd = listd.split()
a, b, c, d = listd
if a == c :
    print('Vertical')
elif b == d :
    print('Horizontal')
else:
    print('Try again')