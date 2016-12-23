import itertools
import string


def p1(p, lines):
    p = bytearray(p)
    for line in lines:
        parts = line.split()
        if line.startswith('swap position'):
            frm, to = int(parts[2]), int(parts[5])
            p[frm], p[to] = p[to], p[frm]
        elif line.startswith('swap letter'):
            frm, to = parts[2], parts[5]
            p = p.translate(string.maketrans(frm + to, to + frm))
        elif line.startswith('rotate right'):
            steps = int(parts[2]) % len(p)
            if not steps % len(p):
                continue
            p = p[-steps:] + p[:len(p) - steps]
        elif line.startswith('rotate left'):
            steps = int(parts[2]) % len(p)
            if not steps % len(p):
                continue
            p = p[steps:] + p[:-(len(p) - steps)]
        elif line.startswith('rotate based'):
            pos = p.index(parts[6])
            steps = (pos + 1 + (pos >= 4)) % len(p)
            if not steps % len(p):
                continue
            p = p[-steps:] + p[:len(p) - steps]
        elif line.startswith('reverse'):
            frm, to = int(parts[2]), int(parts[4]) + 1
            p[frm:to] = p[frm:to][::-1]
        elif line.startswith('move position'):
            frm, to = int(parts[2]), int(parts[5])
            l = p[frm:frm + 1]
            p[frm:frm + 1] = ''
            p[to:to] = l
    return p

# with open('example_21.txt') as f:
#     print p1('abcde', f)
with open('input_21.txt') as f:
    lines = [l.strip() for l in f]
    for c in itertools.permutations('abcdefgh'):
        if p1(''.join(c), lines) == 'fbgdceah':
            print ''.join(c)
            break
