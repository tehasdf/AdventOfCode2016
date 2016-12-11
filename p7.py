import sys


def split(s):
    parts = s.strip().replace(']', '[').split('[')
    return parts[::2], parts[1::2]


def isabba(s):
    return (s[0] == s[3] != s[1]) and s[1] == s[2]


def isbab(s):
    return s[0] == s[2] != s[1]


def groups(s, n=4):
    for i in range(len(s) - n + 1):
        yield s[i:i + n]


def tls(s):
    outside, inside = split(s)
    out_ok = any(isabba(f) for s in outside for f in groups(s))
    in_ok = any(isabba(f) for s in inside for f in groups(s))
    return out_ok and not in_ok


def ssl(s):
    outside, inside = split(s)
    abas = [w for l in outside for w in groups(l, n=3) if isbab(w)]
    babs = [w for l in inside for w in groups(l, n=3) if isbab(w)]
    for a in abas:
        for b in babs:
            if a[0] == b[1] and a[1] == b[0]:
                return True
    return False


assert split('foo[bar]qix[qux]abc') == (['foo', 'qix', 'abc'], ['bar', 'qux'])
assert isabba('abba')
assert not isabba('aaaa')
assert list(groups('abba')) == ['abba']
assert list(groups('aaabcd')) == ['aaab', 'aabc', 'abcd']
assert tls('abba[mnop]qrst')


def p1(f):
    return sum(tls(l) for l in f)


def p2(f):
    return sum(ssl(l) for l in f)

# print p1(sys.stdin)
print p2(sys.stdin)
