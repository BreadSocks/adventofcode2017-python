instructions = map(int, open("input.txt").read().split("\n"))

steps_taken = 0

currentIndex = 0

while len(instructions) > currentIndex >= 0:
    current_value = instructions[currentIndex]
    new_value = current_value + 1
    instructions[currentIndex] = new_value
    currentIndex += current_value
    steps_taken += 1
print steps_taken
