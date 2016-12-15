
discs = [
    (17, 5 + 1),
    (19, 8 + 2),
    (7, 1 + 3),
    (13, 7 + 4),
    (5, 1 + 5),
    (3, 0 + 6),
    (11, 0 + 7)
]


def p1(discs):
    for t in xrange(1, 9999999):
        if all((c + t) % p == 0 for p, c in discs):
            return t


assert p1(discs[:-1]) == 16824  # part 1
assert p1(discs) == 3543984  # part 2
