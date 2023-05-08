angles = input()
angles = angles.split()
if len(angles) == 3:
    x = int(angles[0])
    y = int(angles[1])
    z = int(angles[2])
    if 0 < x < 180 and  0 < y < 180 and 0 < z < 180:
        if x + y + z == 180:
            print ('Yes')
        else: 
            print ('No')
    else: 
        print ('No')