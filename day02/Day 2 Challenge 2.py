import itertools

diffs = []

# ('1098', '122') 9.0 - 5th line

with open("input.txt") as inputFile:
    for line in inputFile:
        line = line.replace("\n", "")
        numbers = map(int, line.split())
        combinations = itertools.combinations(numbers, 2)
        for subset in combinations:
            biggest = max(subset)
            smallest = min(subset)
            if biggest % smallest == 0:
                diffs.append(biggest / smallest)
    print sum(diffs)
