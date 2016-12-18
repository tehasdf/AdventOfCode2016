inp = '^..^^.^^^..^^.^...^^^^^....^.^..^^^.^.^.^^...^.^.^.^.^^.....^.^^.^.^.^.^.^.^^..^^^^^...^.....^....^.'  # NOQA


def nextstate(inp):
    inp = '.{}.'.format(inp)
    for t in zip(inp, inp[1::], inp[2::]):
        t = ''.join(t)
        yield '^' if t in {'^^.', '.^^', '^..', '..^'} else '.'  # Rule 90


def p1(line, rows):
    total = 0
    for _ in xrange(rows):
        total += line.count('.')
        line = ''.join(nextstate(line))
    return total

assert p1('.^^.^.^^^^', 10) == 38
print p1(inp, 40)
print p1(inp, 400000)
