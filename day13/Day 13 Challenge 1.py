instructions = open("input.txt").read().strip().split("\n")
instructions_dict = dict()
for line in instructions:
    parts = line.split(": ")
    instructions_dict[int(parts[0])] = int(parts[1])

print instructions_dict


class Layer:

    def __init__(self, depth, scanner_range):
        self.depth = depth
        self.scanner_range = scanner_range
        self.index = 0
        self.direction = "down"

    def travel(self):
        if self.index == 0:
            self.direction = "down"
        elif self.index == -self.scanner_range + 1:
            self.direction = "up"

        if self.direction == "up":
            self.index += 1
        else:
            self.index -= 1

    def caught_you(self):
        return self.index == 0

    def __repr__(self):
        return "index - " + str(self.index) + " scanner - " + str(self.scanner_range)


last_digit = instructions_dict.keys()[-1] + 1

firewall = []

for x in range(0, last_digit):
    if x in instructions_dict:
        firewall.append(Layer(x, instructions_dict[x]))
    else:
        firewall.append(None)

player_position = -1
caught = 0
print firewall

for x in range(0, last_digit):

    player_position += 1

    for j in firewall:
        if isinstance(j, Layer):
            if j.depth == player_position and j.index == 0:
                caught += (j.depth * j.scanner_range)
            j.travel()
    print firewall


print "\n"
print caught
print player_position