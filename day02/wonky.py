import itertools

line = "1123	104	567	1098	286	665	1261	107	227	942	1222	128	1001	122	69	139"

print len(line.split())

sets = itertools.combinations(line.split(), 2)
for set in sets:
    print set, float(set[0]) / int(set[1])