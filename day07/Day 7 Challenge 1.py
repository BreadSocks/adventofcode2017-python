names = []
with open("input.txt") as inputFile:
    for line in inputFile:
        if line.__contains__("->"):
            parts = line.split(" -> ")
            first_part = parts[0].replace("(", "").replace(")", "").split()
            second_part = parts[1].strip("\n").split(", ")
            for element in second_part:
                names.append(element)
            names.append(first_part[0])
        else:
            parts = line.replace("(", "").replace(")", "").split()
            names.append(parts[0])
names_set = set()
for name in names:
    if name not in names_set:
        names_set.add(name)
    else:
        names_set.remove(name)
print list(names_set)
