listX = input()
listY = input()
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
listX = (listX.split(','))
listX[0] = (listX[0])[1]
listX[4] = (listX[4])[0]
# listX = map(int, listX)
listY = (listY.split(','))
listY[0] = (listY[0])[1]
listY[4] = (listY[4])[0]
# listY = map(int, listY)
for i in range(5):
    list1.append(int(listY[i]) * int(listX[0]))
for i in range(5):
    list2.append(int(listY[i]) * int(listX[1]))
for i in range(5):
    list3.append(int(listY[i]) * int(listX[2]))
for i in range(5):
    list4.append(int(listY[i]) * int(listX[3]))
for i in range(5):
    list5.append(int(listY[i]) * int(listX[4]))
l1 = '[%i,%i,%i,%i,%i]' %(list1[0],list1[1],list1[2],list1[3],list1[4])
l2 = '[%i,%i,%i,%i,%i]' %(list2[0],list2[1],list2[2],list2[3],list2[4])
l3 = '[%i,%i,%i,%i,%i]' %(list3[0],list3[1],list3[2],list3[3],list3[4])
l4 = '[%i,%i,%i,%i,%i]' %(list4[0],list4[1],list4[2],list4[3],list4[4])
l5 = '[%i,%i,%i,%i,%i]' %(list5[0],list5[1],list5[2],list5[3],list5[4])
lF = '[%s,%s,%s,%s,%s]' %(l1,l2,l3,l4,l5)
print(lF)