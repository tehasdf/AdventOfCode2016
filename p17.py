import hashlib


def make_next_states(state):
    inp, (x, y) = state
    d = [l in 'bcdef' for l in hashlib.md5(inp).hexdigest()[:4]]
    for o, l, (xd, yd) in zip(d, 'UDLR', [(0, -1), (0, 1), (-1, 0), (1, 0)]):
        if o and (0 <= x + xd <= 3) and (0 <= y + yd <= 3):
            yield inp + l, (x + xd, y + yd)


def p1(inp):
    states = [(inp, (0, 0))]
    highest = 0
    for i in xrange(1, 99999999):
        next_states = []
        for state in states:
            for nextstate in make_next_states(state):
                if nextstate[1] == (3, 3):
                    highest = i  # part1: return nextstate
                else:
                    next_states.append(nextstate)
        states = next_states
        if not states:
            return highest


# print p1('ihgpwlah')
print p1('gdjjyniy')
