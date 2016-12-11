a = """L1, L5, R1, R3, L4, L5, R5, R1, L2, L2, L3, R4, L2, R3, R1, L2, R5, R3, L4, R4, L3, R3, R3, L2, R1, L3, R2, L1, R4, L2, R4, L4, R5, L3, R1, R1, L1, L3, L2, R1, R3, R2, L1, R4, L4, R2, L189, L4, R5, R3, L1, R47, R4, R1, R3, L3, L3, L2, R70, L1, R4, R185, R5, L4, L5, R4, L1, L4, R5, L3, R2, R3, L5, L3, R5, L1, R5, L4, R1, R2, L2, L5, L2, R4, L3, R5, R1, L5, L4, L3, R4, L3, L4, L1, L5, L5, R5, L5, L2, L1, L2, L4, L1, L2, R3, R1, R1, L2, L5, R2, L3, L5, L4, L2, L1, L2, R3, L1, L4, R3, R3, L2, R5, L1, L3, L3, L3, L5, R5, R1, R2, L3, L2, R4, R1, R1, R3, R4, R3, L3, R3, L5, R2, L2, R4, R5, L4, L3, L1, L5, L1, R1, R2, L1, R3, R4, R5, R2, R3, L2, L1, L5"""  # NOQA


def locations(inp):
    parts = [p.strip() for p in inp.split(',')]
    parts = [(p[0], int(p[1:])) for p in parts if p]

    direction = 'N'
    x, y = 0, 0
    yield 0, 0
    for turn, dist in parts:
        if turn == 'L':
            direction = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}[direction]
        elif turn == 'R':
            direction = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}[direction]
        else:
            raise ValueError('turn: {0}'.format(turn))

        for i in range(dist):
            if direction == 'N':
                y += 1
            elif direction == 'S':
                y -= 1
            elif direction == 'W':
                x -= 1
            elif direction == 'E':
                x += 1
            yield x, y


def distance(pos):
    x, y = pos
    return abs(x) + abs(y)


def p1(inp):
    for pos in locations(inp):
        pass
    return distance(pos)


def p2(inp):
    visited = set()
    for pos in locations(inp):
        print pos
        if pos in visited:
            return distance(pos)
        visited.add(pos)


# assert p1('R2, L3') == 5
# assert p1('R2, R2, R2') == 2
# assert p1('R5, L5, R5, R3') == 12
assert p1(a) == 253

# assert p2('R8, R4, R4, R8') == 4

# print p2(a)
