# the "fuck readability" edition
import hashlib


def make_next_states((inp, (x, y))):
    d = [l in 'bcdef' for l in hashlib.md5(inp).hexdigest()[:4]]
    for o, l, (xd, yd) in zip(d, 'UDLR', [(0, -1), (0, 1), (-1, 0), (1, 0)]):
        if o and (0 <= x + xd <= 3) and (0 <= y + yd <= 3):
            yield inp + l, (x + xd, y + yd)


def _winning_states(states):
    while states:
        for steps, pos in make_next_states(states.pop()):
            (yield steps) if pos == (3, 3) else states.append((steps, pos))


def p1(inp, part=1):
    return {1: min, 2: max}[part](_winning_states([(inp, (0, 0))]), key=len)

print p1('gdjjyniy', part=2)
