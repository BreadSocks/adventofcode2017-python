import sys

sys.setrecursionlimit(50000)
pipes_input = open("input.txt").read().split("\n")

pipes = dict()
for line in pipes_input:
    parts = line.split(" <-> ")
    connections = parts[1].strip().split(", ")
    pipes[parts[0]] = connections

connected_pipes = ["0"]


def find_connections_mk2(entries):
    found = []
    for entry in entries:
        pipe_entry = pipes[entry]
        for pipe in pipe_entry:
            if pipe not in connected_pipes and pipe not in found:
                found.append(pipe)
                connected_pipes.append(pipe)
    if len(found) > 0:
        print found
        find_connections_mk2(found)
    else:
        print "stopped"


find_connections_mk2(["0"])
connected_pipes = map(int, connected_pipes)
connected_pipes = sorted(connected_pipes)

print "length", len(connected_pipes)
