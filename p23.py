

def p1(inp):
    r = dict.fromkeys('abcd', 0)
    r['a'] = 12
    def getval(x):
        return r[x] if x in r else int(x)

    instrs = []
    for line in inp:
        parts = line.strip().split()
        cmd = parts[0]
        instrs.append([cmd, parts[1:]])
    i = 0
    c = 0
    import pudb; pu.db  # NOQA
    while i < len(instrs):
        if instrs[i:i + 5] == [
            ['inc', ['a']],
            ['dec', ['c']],
            ['jnz', ['c', '-2']],
            ['dec', ['d']],
            ['jnz', ['d', '-5']]
        ]:
            r['a'] += getval('c') * getval('d')
            i += 5
            continue
        cmd, args = instrs[i]
        if cmd == 'cpy':
            if args[1] in r:
                r[args[1]] = getval(args[0])
        elif cmd == 'jnz':
            if getval(args[0]):
                i += getval(args[1]) - 1
        elif cmd == 'dec':
            r[args[0]] -= 1
        elif cmd == 'inc':
            r[args[0]] += 1
        elif cmd == 'tgl':
            pos = i + getval(args[0])
            if pos >= len(instrs):
                i += 1
                c += 1
                if c % 100000 == 0:
                    print c, i, r
                continue
            tgt = instrs[pos]
            if len(tgt[1]) == 2:
                tgt[0] = 'cpy' if tgt[0] == 'jnz' else 'jnz'
            elif len(tgt[1]) == 1:
                tgt[0] = 'dec' if tgt[0] == 'inc' else 'inc'

        i += 1
        c += 1
        if c % 100000 == 0:
            print c, i, r
    return r['a']


with open('input_23.txt') as f:
    print p1(f)
