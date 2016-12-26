from collections import deque
from itertools import combinations, permutations


def steps(board, pos, target):
    def _nextpos((x, y)):
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            if board[y + dy][x + dx] != '#':
                yield (x + dx, y + dy)
    seen = set()
    steps = 0
    states = deque([pos])
    while True:
        steps += 1
        nextstates = []
        for currstate in states:
            for nextpos in _nextpos(currstate):
                if nextpos == target:
                    return steps
                if nextpos in seen:
                    continue
                seen.add(nextpos)
                nextstates.append(nextpos)
        states = nextstates


def _permute(digits, part=2):
    for p in permutations(digits - {'0'}):
        if part == 2:
            yield '0' + ''.join(p) + '0'
        elif part == 1:
            yield '0' + ''.join(p)


def p1(lines, part=2):
    board = [l.strip() for l in lines]
    digits = {x for x in ''.join(board) if x.isdigit()}
    pos = {}
    for y, l in enumerate(board):
        for d in digits:
            if d in l:
                pos[d] = l.index(d), y
    s = {}
    for start, end in combinations(digits, 2):
        s[start, end] = s[end, start] = steps(board, pos[start], pos[end])

    return min(
        sum(s[a, b] for a, b in zip(p, p[1:]))
        for p in _permute(digits, part=part))

# with open('example_24.txt') as f:
#     print p1(f)

with open('input_24.txt') as f:
    print p1(f)
