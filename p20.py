def p1(blocked):
    for a, b in zip(blocked, blocked[1::]):
        if b[0] > a[1] + 1 and not any(l <= a[1] + 1 <= h for l, h in blocked):
                return a[1] + 1


def p2(blocked):
    merged = []
    for l, h in blocked:
        for i, (el, eh) in enumerate(merged):
            if el <= l <= eh or el <= h <= eh:
                merged[i] = (min(el, l), max(eh, h))
                break
        else:
            merged.append((l, h))
    return 2**32 - sum(h - l + 1 for l, h in merged)


with open('input_20.txt') as f:
    print p1(sorted(map(int, x.split('-')) for x in f))


with open('input_20.txt') as f:
    print p2(sorted(map(int, x.split('-')) for x in f))
