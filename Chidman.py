n = int(input())
heights = []
diff = []
listd = []
for i in range (1, n+1):
    heights.append(int(input()))
normal = int(sum(heights)/n)
for h in heights:
    diff.append(h-normal)
for d in diff:
    if d > 0:
        listd.append(d)
print(sum(listd))