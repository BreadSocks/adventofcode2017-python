data = open("input.txt").read()

example1 = "1122"
example2 = "1111"
example3 = "1234"
example4 = "91212129"

total = 0

input = data

for index, character in enumerate(input):
    if index == len(input) - 1:
        if character == input[0]:
            total += int(character)
        else:
            continue
    elif character == input[index + 1]:
        total += int(character)
print total
