inp1 = float(input().split(': ')[1])
opr = (input().split(': ')[1])
inp2 = float(input().split(': ')[1])

oprs = ['*', '+', '-', '/']
if opr in oprs:
    if opr == oprs[0]:
        res = inp1 * inp2
    elif opr == oprs[1]:
        res = inp1 + inp2
    elif opr == oprs[2]:
        res = inp1 - inp2
    else:
        res = inp1 / inp2
else:
    res = 'Invalid operator - please try \nagain.'

print(res)