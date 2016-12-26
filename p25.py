

def p1(inp, start_a=12):
    r = dict.fromkeys('abcd', 0)
    r['a'] = start_a

    def getval(x):
        return r[x] if x in r else int(x)

    instrs = []
    for line in inp:
        parts = line.strip().split()
        cmd = parts[0]
        instrs.append([cmd, parts[1:]])
    i = 0
    prevstates = set()
    emitted = []
    while i < len(instrs):
        cmd, args = instrs[i]
        if cmd == 'cpy' and args[1] in r:
            r[args[1]] = getval(args[0])
        elif cmd == 'jnz' and getval(args[0]):
            i += getval(args[1]) - 1
        elif cmd == 'dec':
            r[args[0]] -= 1
        elif cmd == 'inc':
            r[args[0]] += 1
        elif cmd == 'out':
            state = tuple(r[x] for x in 'abcd')
            if state in prevstates:
                return emitted
            prevstates.add(state)
            emitted.append(getval(args[0]))
        i += 1


with open('input_25.txt') as f:
    lines = list(f)
    for r in range(9999):
        pattern = p1(lines, start_a=r)
        if len(pattern) % 2 == 0 and set(pattern[::2]) == {0} \
                and set(pattern[1::2]) == {1}:
            print r, pattern
            break
