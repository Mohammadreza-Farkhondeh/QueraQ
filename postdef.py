# Getting inputs
IDs = input().split()
temp = []
for i in IDs:
    if i not in temp and len(i) == 4:
        temp.append(i)
IDs = temp

territories = input().split()

terriCode = input().split(", ")
for i in range(len(terriCode)):
    terriCode[i] = terriCode[i].split()

terriWage = input().split()
for q in range(len(terriWage)):
    terriWage[q] = float(terriWage[q])

postmanName = input().split()

postmanDestination = input().split(", ")
for k in range(len(postmanDestination)):
    postmanDestination[k] = postmanDestination[k].split()
    postmanDestination[k].sort()


boxPost = []
Invalid = []
for e in range(len(territories)):
    boxPost.append([])
for x in range(len(IDs)):
    flags = True
    for f in range(len(territories)):
        if IDs[x][0:2] in terriCode[f]:
            boxPost[f].append(IDs[x])
            flags = False
    if flags:
        Invalid.append(IDs[x])


postman_in_distinct = []
for i in territories:
    postman_in_distinct.append([])
for j in range(len(territories)):
    for k in range(len(postmanDestination)):
        if territories[j] in postmanDestination[k]:
            postman_in_distinct[j].append(postmanName[k])

res = []
for i in range(len(postmanName)):
    res.append([])
for k in range(len(boxPost)):
    if len(postman_in_distinct[k]) == 1:
        a = postmanName.index(postman_in_distinct[k][0])
        for j in range(len(boxPost[k])):
            res[a].append(boxPost[k][j])
    else:
        counter = []
        for i in range(len(postman_in_distinct[k])):
            counter.append(0)
        for j in range(len(boxPost[k])):
            a = counter.index(min(counter))
            res[a].append(boxPost[k][j])
            counter[a] += 1


for i in range(len(res)):
    res[i].sort()


postmanNameAlpha = postmanName.copy()
postmanNameAlpha.sort()

for m in range(len(postmanNameAlpha)):
    wage = 0.0
    b = postmanName.index(postmanNameAlpha[m])
    print(f"{postmanNameAlpha[m]}:")
    for o in range(len(postmanDestination[b])):
        e = territories.index(postmanDestination[b][o])
        print(f"{postmanDestination[b][o]}:")
        print("    ", end="")
        z = territories.index(postmanDestination[b][o])
        for t in range(len(res[b])):
            if res[b][t][0:2] in terriCode[z]:
                print(res[b][t], end=" ")
                wage += terriWage[z]
        print()
    print(f"Wage = ${wage}")
    print()
    print()


print("Invalid postal codes:")
print("    ", end="")
for i in Invalid:
    print(i, end=" ")

