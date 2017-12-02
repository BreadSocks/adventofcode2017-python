min_found = 0
max_found = 0

diffs = []

with open("input.txt") as inputFile:
    for line in inputFile:
        line = line.replace("\n", "")
        numbers = line.split()
        for number in numbers:
            intNumber = int(number)
            if min_found == 0 or intNumber < min_found:
                min_found = intNumber
            if intNumber > max_found:
                max_found = intNumber
        diffs.append(max_found - min_found)
        min_found = 0
        max_found = 0
    print sum(diffs)
