import itertools
import numpy as np

N, M = map(int, input().split())

matrix = np.zeros((N,N), dtype=int)
for i in range(N):
    matrix[i] = np.array(list(map(int, input().split())))

trips = []
for j in range(M):
    blist = [0, 0]
    blist[0], blist[1] = list(map(int, input().split()))
    trips.append(blist)

cost = matrix[[trip[0]-1 for trip in trips], [trip[1]-1 for trip in trips]].sum()

clist = list(map(int, input().split('-')))
s = clist[-1]
clist = clist[:-1]
clist = list(set(clist))


all_subsets = []
for k in range(len(clist) + 1):
    all_subsets.extend(itertools.combinations(clist, k))
all_subsets = [list(s) for s in all_subsets]

x = sum([sum(subset)%s == 0 for subset in all_subsets])

print(cost, x)
