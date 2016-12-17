import hashlib


def make_next_states(state):
    inp, (x, y) = state
    d = [l in 'bcdef' for l in hashlib.md5(inp).hexdigest()[:4]]
    for o, l, (xd, yd) in zip(d, 'UDLR', [(0, -1), (0, 1), (-1, 0), (1, 0)]):
        if o and (0 <= x + xd <= 3) and (0 <= y + yd <= 3):
            yield inp + l, (x + xd, y + yd)


def _winning_states(inp):
    states = [(inp, (0, 0))]
    while states:
        for steps, pos in make_next_states(states.pop()):
            if pos == (3, 3):
                yield steps
            else:
                states.append((steps, pos))


def p1(inp):
    return max(_winning_states(inp), key=len)  # s/max/min/ for part 1

# print p1('ihgpwlah')
print p1('gdjjyniy')
