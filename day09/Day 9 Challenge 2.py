inputFile = open("input.txt").read()

example1 = "<>"  # 0 characters.
example2 = "<random characters>"  # 17 characters.
example3 = "<<<<>"  # 3 characters.
example4 = "<{!>}>"  # 2 characters.
example5 = "<!!>"  # 0 characters.
example6 = "<!!!>>"  # 0 characters.
example7 = "<{o\"i!a,<{i<a>"  # 10 characters.

source = inputFile

in_garbage = False
in_group = False
inner_brackets = 0
index = 0
garbage_characters_removed = 0
while index < len(source):
    character = source[index]
    if character == "!":
        index += 1
    elif character == "<" and not in_garbage:
        in_garbage = True
    elif character == ">":
        in_garbage = False
    elif in_garbage:
        garbage_characters_removed += 1
    index += 1

print garbage_characters_removed
