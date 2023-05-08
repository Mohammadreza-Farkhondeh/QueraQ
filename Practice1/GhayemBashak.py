#Getting Inputs and Values

Floors, RoomsPF = map(int, input().split())
A_floor, A_room = map(int, input().split())
B_floor, B_room = map(int, input().split())
C_floor, C_room = map(int, input().split())
speed = 2


#defining Manhatten_Distance of a point drom origin function for n-dimensional space

def Manhatten_Distance(*arg):
    args = [i for i in arg]
    origin = [0 for i in arg]
    D = 0
    for a in range(len(args)):
        D += abs(args[a] - origin[a])
    return(D)


#Calculating Manhatten distances of given points via function defined perviously

dA = Manhatten_Distance(A_floor, A_room)
dB = Manhatten_Distance(B_floor, B_room)
dC = Manhatten_Distance(C_floor, C_room)
Ds = [dA, dB, dC]


#Geting the smallest Manhatten distance of points given and printing time to reach and the Manhatten distance

minD = min(Ds)
if minD < 8:
    print(speed * minD)
else:
    print('Game Over!')
