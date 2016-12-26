from collections import deque


def p1(a):
    e = deque(xrange(1, a + 1))
    while len(e) > 1:
        e.rotate(-1)
        e.popleft()
    return e


def p2(n):
    e = deque(xrange(1, n + 1))
    e.rotate(-(n // 2))
    while len(e) > 1:
        e.popleft()
        if len(e) % 2 == 0:
            e.rotate(-1)
    return e

print p2(3001330)
# print p2(3014603)
