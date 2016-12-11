import re


def p1(inp, part=1):
    inp = ''.join(inp.split())
    total = 0
    while inp:
        m = re.search('\((\d+)x(\d+)\)', inp)
        if not m:
            return total + len(inp)
        x, y = map(int, m.groups())

        if part == 1:
            total += m.start() + x * y
        elif part == 2:
            total += m.start() + p1(inp[m.end():m.end() + x], 2) * y

        inp = inp[m.end() + x:]
    return total


assert p1('ADVENT') == 6
assert p1('A(1x5)BC') == 7
assert p1('(3x3)XYZ') == 9
assert p1('A(2x2)BCD(2x2)EFG') == 11
assert p1('(6x1)(1x3)A') == 6
assert p1('X(8x2)(3x3)ABCY') == 18

with open('input_9.txt') as f:
    print p1(f.read(), part=1)


assert p1('(3x3)XYZ', 2) == 9
assert p1('X(8x2)(3x3)ABCY', 2) == len('XABCABCABCABCABCABCY')
assert p1('(27x12)(20x12)(13x14)(7x10)(1x12)A', 2) == 241920
assert p1('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN', 2) == 445

with open('input_9.txt') as f:
    print p1(f.read(), 2)
