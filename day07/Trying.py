names = []
weights = dict()
names_of_discs = []
tree = {}
with open("input.txt") as inputFile:
    for line in inputFile:
        if line.__contains__("->"):
            parts = line.split(" -> ")
            first_part = parts[0].replace("(", "").replace(")", "").split()
            weights[first_part[0]] = int(first_part[1])
            second_part = parts[1].strip("\n").split(", ")
            second_part_dict = {}
            for element in second_part:
                names.append(element)
                second_part_dict[element] = None
            names.append(first_part[0])
            names_of_discs.append(first_part[0])
            tree[first_part[0]] = second_part_dict
        else:
            parts = line.replace("(", "").replace(")", "").split()
            weights[parts[0]] = int(parts[1])
            names.append(parts[0])
            line_dict = {parts[0]: None}
            tree[line_dict.keys()[0]] = line_dict.values()
names_set = set()
for name in names:
    if name not in names_set:
        names_set.add(name)
    else:
        names_set.remove(name)
print weights
print names_of_discs
print tree

disc_totals = dict()
for disc in names_of_discs:
    totals = [weights[disc]]
    for key in tree[disc]:
        totals.append(weights[key])

    print "Disc: ", disc, "Sum: ", sum(totals), "Elements: ", totals

