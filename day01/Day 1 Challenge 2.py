data = open("input.txt").read()

example1 = "1212"
example2 = "1221"
example3 = "123425"
example4 = "123123"
example5 = "12131415"

total = 0

input = data

for index, character in enumerate(input):
    nextIndex = index + (len(input) / 2)
    if character == input[nextIndex % len(input)]:
        total += int(character)
print total
