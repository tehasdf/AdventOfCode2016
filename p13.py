

def iswall(x, y):
    v = x * x + 3 * x + 2 * x * y + y + y * y + 1362
    return bin(v).count('1') % 2


def moves(x, y):
    yield (x + 1, y)
    yield (x, y + 1)
    if x > 0:
        yield (x - 1, y)
    if y > 0:
        yield (x, y - 1)


pos = (1, 1)

total = 0
seen = set([pos])
count = 0

allseen = set()
while seen:
    allseen |= seen
    print count, len(allseen)
    count += 1
    nextseen = set()
    for pos in seen:
        for move in moves(*pos):
            if not iswall(*move):
                nextseen.add(move)
                if move == (31, 39):
                    raise ValueError(count)

    seen = nextseen
