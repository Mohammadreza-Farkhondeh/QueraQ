X = int(input())
N = int(input())
if N == 0:
    print(20)
if N == 7:
    print(X)
elif N != 0:
    if X > N:
        print(X - N)
    else:
        print(0)