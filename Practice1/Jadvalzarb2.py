#Getting inputs and process them
listX = input()
listY = input()
listX = (listX.split(', '))
listX[0], listX[4] = (listX[0])[1], (listX[4])[0]
listY = (listY.split(', '))
listY[0], listY[4] = (listY[0])[1], (listY[4])[0]
listX = [eval(x) for x in listX]
listY = [eval(x) for x in listY]
listT = [[], [], [], [], []]

#processing the multiplication using a loop
for i in range(5):
    for j in range(5):
        listT[i].append(listX[i]*listY[j])
print(listT)
