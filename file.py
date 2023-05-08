n = int(input())
odds = []
evens = []
square = []
cube = []
for i in range(2, n+1):
    if i % 2 == 0:
        evens.append(i)
    else:
        odds.append(i)
    if ((int(i**(0.5)))**2)  == i:
        square.append(i)
    if ((round(i**(1/3)))**3) == i:
        cube.append(i)
#print(evens, odds, square, cube)
print('Checking numbers from 2 to %i' %n)
print('Odd (%i) : %i...%i' %(len(odds), odds[0], odds[-1]))
print('Even (%i) : %i...%i' %(len(evens), evens[0], evens[-1]))
print('Square : ',square
print('Cube : ' ,cube)
