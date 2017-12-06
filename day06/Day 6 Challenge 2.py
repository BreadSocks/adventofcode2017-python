inputFile = open("input.txt").read()

example = "0 2 7 0"

memory_banks = map(int, inputFile.split())

redistributions = []

while len(redistributions) == len(set(redistributions)):
    biggest_bank = memory_banks.index(max(memory_banks))
    blocks_in_bank = memory_banks[biggest_bank]
    memory_banks[biggest_bank] = 0
    current_bank = biggest_bank
    while blocks_in_bank > 0:
        next_bank_index = 0 if current_bank == len(memory_banks) - 1 else current_bank + 1
        memory_banks[next_bank_index] += 1
        blocks_in_bank -= 1
        current_bank = next_bank_index
    redistributions.append(str(memory_banks))

repeating_element = redistributions[-1]
element_seen = redistributions.index(repeating_element)
print "Loop size : ", len(redistributions) - 1 - element_seen

