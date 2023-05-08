listp = input()
listp = listp.split()
a, b = listp
if int(b) > 10:
    dir = 'Left'
    b = 21 - int(b)
else: 
    dir = 'Right'
print (dir, 11 - int(a), b)