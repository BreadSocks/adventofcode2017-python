inputFile = open("input.txt").read()

example1 = "{}"  # score of 1.
example2 = "{{{}}}"  # score of 1 + 2 + 3 = 6.
example3 = "{{},{}}"  # score of 1 + 2 + 2 = 5.
example4 = "{{{},{},{{}}}}"  # score of 1 + 2 + 3 + 3 + 3 + 4 = 16.
example5 = "{<a>,<a>,<a>,<a>}"  # score of 1.
example6 = "{{<ab>},{<ab>},{<ab>},{<ab>}}"  # score of 1 + 2 + 2 + 2 + 2 = 9.
example7 = "{{<!!>},{<!!>},{<!!>},{<!!>}}"  # score of 1 + 2 + 2 + 2 + 2 = 9.
example8 = "{{<a!>},{<a!>},{<a!>},{<ab>}}"  # score of 1 + 2 = 3.

source = inputFile

in_garbage = False
in_group = False
inner_brackets = 0
score = 0
index = 0
while index < len(source):
    character = source[index]
    if character == "!":
        index += 1
    elif character == "<":
        in_garbage = True
    elif character == ">":
        in_garbage = False
    elif not in_group and character == "{":
        in_group = True
    elif in_group  and not in_garbage and character == "{":
        inner_brackets += 1
    elif in_group and not in_garbage and inner_brackets > 0 and character == "}":
        score += inner_brackets + 1
        inner_brackets -= 1
    elif in_group and not in_garbage and character == "}":
        score += 1
    index += 1

print score
