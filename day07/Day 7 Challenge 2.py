tree = {}
weights = {}
with open("example.txt") as inputFile:
    for line in inputFile:
        if line.__contains__("->"):
            parts = line.split(" -> ")
            first_part = parts[0].replace("(", "").replace(")", "").split()
            weights[first_part[0]] = int(first_part[1])
            second_part = parts[1].strip("\n").split(", ")
            second_part_dict = {}
            for element in second_part:
                second_part_dict[element] = None
            tree[first_part[0]] = second_part_dict
        else:
            parts = line.replace("(", "").replace(")", "").split()
            weights[parts[0]] = int(parts[1])
            line_dict = {parts[0]: None}
            tree[line_dict.keys()[0]] = line_dict.values()
print tree
print weights


def find_home(k, v):
    print k, v


def found_home(k, data):
    for kk, vv in data.items():
        if isinstance(vv, dict):
            if k in vv:
                yield vv
            else:
                find_home(k, vv)
    print "found master key", k

for key, value in tree.items():
    if isinstance(value, dict):
        tree[key] = found_home(key, value)
        found_home(key, value)
print tree
