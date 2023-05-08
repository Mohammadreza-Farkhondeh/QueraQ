import math
a = float(input())
b = float(input())
c = float(input())
Delta = (b**2)-4*a*c
if a != 0:
    if Delta > 0:
        x_1 = (-b + math.sqrt(Delta)) / (2 * a)
        x_2 = (-b - math.sqrt(Delta)) / (2 * a)
        print('{:.3f}'.format(x_2))
        print('{:.3f}'.format(x_1))
    elif Delta == 0:
        x = -b / (2 * a)
        print('{:.3f}'.format(x))
    else:
        print('IMPOSSIBLE')
elif b != 0:
    x = -(c/b)
    print('{:.3f}'.format(x))
    
else:
    print('IMPOSSIBLE')
