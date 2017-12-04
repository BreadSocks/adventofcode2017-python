correctLines = 0
with open("input.txt") as inputFile:
    for line in inputFile:
        unsorted_words = line.split()
        sorted_words = []
        for word in unsorted_words:
            sorted_words.append(''.join(sorted(word)))
        if len(unsorted_words) == len(set(sorted_words)):
            correctLines += 1
print correctLines
