IDsP = input().split()
Destination_names = input().split()
Destination_codes = input().split(', ')
Destination_wages = list(map(float, input().split(' ')))
Man_names = input().split()
Man_area = input().split(', ')

IDs = set([ID for ID in IDsP if len(ID) == 4])
Destination_codes = [list(map(int, codes.split())) for codes in Destination_codes]
Man_area = [areas.split() for areas in Man_area]
Man_boxes = [[] for i in range(len(Man_names))]
Destinations = list(zip(Destination_names, Destination_codes, Destination_wages))
Mans = list(zip(Man_names, Man_area, Man_boxes))


invalids = []
for ID in IDs:
    valid = False
    for dest in Destinations:
        if int(str(ID)[:2]) in dest[1]:
            valid = True
            break
    if not valid:
        invalids.append(ID)
for invalid in invalids:
    IDs.remove(invalid)
IDs = sorted(IDs)

plan = {}
for i in Mans:
    plan.update({i[0]: []})

for ID, man in zip(IDs, Mans):
    plan[man[0]].append(ID)






x = 2