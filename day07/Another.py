import pprint

names = []
weights = dict()
names_of_discs = []
flat_tree = {}
with open("input.txt") as inputFile:
    for line in inputFile:
        if line.__contains__("->"):
            parts = line.split(" -> ")
            first_part = parts[0].replace("(", "").replace(")", "").split()
            weights[first_part[0]] = int(first_part[1])
            second_part = parts[1].strip("\n").split(", ")
            second_part_dict = {}
            for element in second_part:
                names.append(element)
                second_part_dict[element] = None
            names.append(first_part[0])
            names_of_discs.append(first_part[0])
            flat_tree[first_part[0]] = second_part_dict
        else:
            parts = line.replace("(", "").replace(")", "").split()
            weights[parts[0]] = int(parts[1])
            names.append(parts[0])
            line_dict = {parts[0]: None}
            flat_tree[line_dict.keys()[0]] = line_dict.values()
names_set = set()
for name in names:
    if name not in names_set:
        names_set.add(name)
    else:
        names_set.remove(name)


def construct_tree(key):
    found = flat_tree[key]
    if isinstance(found, dict):
        for next_key in found:
            found[next_key] = construct_tree(next_key)
    return found


tree = dict()
trunk = list(names_set)[0]
tree[trunk] = construct_tree(trunk)
pp = pprint.PrettyPrinter()
pp.pprint(tree)


def put_numbers_in(element):
    for key, value in element.iteritems():
        if isinstance(value, dict):
            put_numbers_in(value)
        else:
            element[key] = weights[key]
    print element

put_numbers_in(tree)

pp.pprint(tree)

testing = dict()


def find_numbers_int(element, parent_key):
    for key, value in element.iteritems():
        if isinstance(value, dict):
            find_numbers_int(value, key)
        else:
            print "Parent:", parent_key, "Parent Weight:", weights[parent_key], "Child:", key, "Child Weight:", weights[key]
        if parent_key in testing:
            testing[parent_key] += weights[key]
        else:
            testing[parent_key] = weights[key]
    testing[parent_key] += weights[parent_key]

find_numbers_int(tree, trunk)

pp.pprint(testing)

# for key1, value1 in tree.iteritems():
#     if isinstance(value1, dict):
#         total1 = 0
#         for key2, value2 in value1.iteritems():
#             if isinstance(value2, dict):
#                 total2 = 0
#                 for key3, value3 in value2.iteritems():
#                     if isinstance(value3, dict):
#                         total3 =
#
#                     else:
#                         total2 += weights[key3]
#                         tree[key1][key2][key3] = weights[key3]
#
# pp.pprint(tree)




# def print_it_2(key):
#     found = tree[key]:
#     if isinstance(found, dict):
#         for next_key in found:
#             if isinstance()
#
#
# def print_it(dictionary):
#     total = 0
#     for keyy, valuee in dictionary.iteritems():
#         if isinstance(valuee, dict):
#             total += print_it(valuee)
#         else:
#             total += weights[keyy]
#         return total
#     print total
#
#
# def print_tree(key, dictionary):
#     found = dictionary[key]
#     if isinstance(found, dict):
#         total = 0
#         print found
#         for next_key, next_value in found:
#             if isinstance(next_value, dict):
#                 total += print_tree(next_key, found)
#             else:
#                 total += weights[next_key]
#         print key, total
#         return total