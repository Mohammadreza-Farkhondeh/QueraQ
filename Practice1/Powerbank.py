target = int(input())
a, b = map(int, input().split())
t = 0
value = 0
while value < target:
    if t % 2 == 0:
        value += a
        t += 1
    else:
        value -= b
        t += 1
if t % 2 == 0:
    t /= 2
else:
    t = int(t/2 + 0.5)
print(t)