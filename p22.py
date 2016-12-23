import sys


def parse(inp):
    nodes = {}
    for line in inp:
        if not line.startswith('/dev/grid'):
            continue
        parts = line.strip().split()
        used, avail = int(parts[2][:-1]), int(parts[3][:-1])
        nameparts = parts[0].split('-')
        pos = int(nameparts[1][1:]), int(nameparts[2][1:])
        nodes[pos] = used, avail
    return nodes


def pairs(nodes):
    count = 0
    empty = set()
    for node, (used, avail) in nodes.items():
        for node2, (used2, avail2) in nodes.items():
            if node == node2 or used == 0:
                continue
            if used <= avail2:
                count += 1
                empty.add(node)
    return empty


def n(pos):
    x, y = pos
    if x > 0:
        yield (x - 1, y)
    if y > 0:
        yield (x, y - 1)
    yield (x + 1, y)
    yield (x, y + 1)

with open('input_22.txt') as f:
    nodes = parse(f)

topx, topy = max(x for x, y in nodes), max(y for x, y in nodes)
empty = pairs(nodes)

goal = topx, 0

# print topx, topy
for y in range(topy + 1):
    for x in range(topx + 1):
        if (x, y) == (22, 25):
            sys.stdout.write('_')
        elif (x, y) in empty:
            sys.stdout.write('.')
        else:
            sys.stdout.write('#')
    sys.stdout.write('\n')

# # 22, 25
