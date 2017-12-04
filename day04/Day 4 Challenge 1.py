correctLines = 0
with open("input.txt") as inputFile:
    for line in inputFile:
        parts = line.split()
        words = set(parts)
        if len(words) == len(parts):
            correctLines += 1
print correctLines
