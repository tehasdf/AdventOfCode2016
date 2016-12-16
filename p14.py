import hashlib
import re


def p1(salt, rounds=1, cachesize=25000):
    hashcache = []

    for ix in xrange(cachesize):
        h = '{}{}'.format(salt, ix)
        for _ in xrange(rounds):
            h = hashlib.md5(h).hexdigest()
        hashcache.append(h)

    ix = 0
    found = 0
    while found < 64:
        m = re.search('(.)\\1\\1', hashcache[ix])
        ix += 1
        if m:
            c = m.group(0)[0] * 5
            found += any(c in h for h in hashcache[ix:ix + 1000])
    return ix - 1

# print p1('abc')
print p1('zpqevtbw')
