import sys


def p1(inp, part=1):
    r = dict.fromkeys('abcd', 0)
    if part == 2:
        r['c'] = 1

    def getval(x):
        return r[x] if x in r else int(x)

    instrs = []
    for line in inp:
        parts = line.strip().split()
        cmd = parts[0]
        instrs.append((cmd, parts[1:]))
    i = 0
    while i < len(instrs):
        cmd, args = instrs[i]
        if cmd == 'cpy':
            r[args[1]] = getval(args[0])
        elif cmd == 'jnz':
            if getval(args[0]):
                i += getval(args[1]) - 1
        elif cmd == 'dec':
            r[args[0]] -= 1
        elif cmd == 'inc':
            r[args[0]] += 1
        i += 1
    return r['a']


print p1(sys.stdin, part=2)
