import re
import sys
import numpy


def display(inp, size):
    lcd = numpy.zeros(size)
    for line in inp:
        if line.startswith('rect'):
            parts = re.search('rect (\d+)x(\d+)', line)
            x, y = map(int, parts.groups())
            lcd[0:y, 0:x] = 1
        elif line.startswith('rotate'):
            parts = re.search('rotate (\w+) .=(\d+) by (\d+)', line)
            what, pos, shift = parts.groups()
            pos, shift = int(pos), int(shift)
            if what == 'column':
                lcd[:, pos] = numpy.roll(lcd[:, pos], shift)
            else:
                lcd[pos] = numpy.roll(lcd[pos], shift)
    return lcd


def p1(inp, size=(6, 50)):
    return display(inp, size).sum()


def p2(inp, size=(6, 50)):
    return '\n'.join(''.join('#' if x else ' 'for x in row)
                     for row in display(inp, size))


# print p1(sys.stdin)
print p2(sys.stdin)
