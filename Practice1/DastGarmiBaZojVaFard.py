n = int(input())
list = []
while len(list) < 7:
    if n % 2 == 0:
        n /= 2
        list.append(int(n))
    else:
        n = 3*(n+1)
        list.append(int(n))
print('[%i,%i,%i,%i,%i,%i,%i]'%(list[0],list[1],list[2],list[3],list[4],list[5],list[6]))
