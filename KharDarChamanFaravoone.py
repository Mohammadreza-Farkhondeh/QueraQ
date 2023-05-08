a, b, l = map(int, input().split())
time = 0
Round = 0
while Round < l:
    if Round % 2 == 0:
        time += a
        Round += 1
    else:
        time += b
        Round += 1
if Round == l:
    print (time)


    
