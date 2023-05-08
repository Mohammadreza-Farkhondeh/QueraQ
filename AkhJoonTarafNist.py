a_3 = int(input())
days1 = input().split( )
a_2 = int(input())
days2 = input().split( )
a_2 = int(input())
days3 = input().split( )
alldays = ['shanbe', '1shanbe', '2shanbe', '3shanbe', '4shanbe', '5shanbe', 'jome']
listdays = []
[listdays.append(x) for x in days1 if x not in listdays]
[listdays.append(x) for x in days2 if x not in listdays]
[listdays.append(x) for x in days3 if x not in listdays]
print(len(set(alldays)-set(listdays)))