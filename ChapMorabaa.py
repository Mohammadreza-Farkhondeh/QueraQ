n = int(input())
line = 0
while line < n:
    if line == 0 or line == (n-1):
        print(n * '*')
    else:
        print('*' + (n-2) * ' ' + '*')
    line += 1