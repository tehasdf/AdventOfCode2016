from collections import Counter


def split(name):
    name, _, sector_checksum = name.strip().rpartition('-')
    sector, _, checksum = sector_checksum.partition('[')
    checksum = checksum[:-1]
    return name, int(sector), checksum


def real(name, checksum):
    letters = Counter(name.replace('-', ''))
    return ''.join(sorted(letters, key=lambda x: (-letters[x], x))[:5]) \
        == checksum


def decrypt(name, counter):
    def letters():
        for letter in name:
            if letter == '-':
                yield ' '
            else:
                x = ord(letter) - ord('a')
                x = (x + counter) % 26
                yield chr(x + ord('a'))
    return ''.join(letters())


def p1(inp):
    return sum(sector for name, sector, checksum in map(split, inp)
               if real(name, checksum))


def p2(inp):
    for line in inp:
        name, sector, checksum = split(line)
        name = decrypt(name, sector)
        if 'north' in name:
            print sector, name


assert real('aaaaa-bbb-z-y-x', 'abxyz')
assert real('a-b-c-d-e-f-g-h', 'abcde')
assert real('not-a-real-room', 'oarel')
assert not real('totally-real-room', 'decoy')

with open('input_4.txt') as f:
    print p1(f)

assert decrypt('q', 343) == 'v'
assert decrypt('qzmt-zixmtkozy-ivhz', 343) == 'very encrypted name'

with open('input_4.txt') as f:
    print p2(f)
