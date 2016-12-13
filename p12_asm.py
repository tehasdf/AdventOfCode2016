# python p12_asm.py <input_12.txt > foo.asm && nasm -felf64 foo.asm && gcc foo.o && ./a.out
import sys

PREAMBLE = """global  main
extern printf

format:
        db  "%d", 10, 0
main:
        xor r8, r8
        xor r9, r9
        mov r10, {}
        xor r11, r11
"""

PRINTF = """
        mov rdi, format
        mov rsi, r8
        mov rax, 0
        call printf
        ret"""


def _code(ix, line):
    names = {'a': 'r8', 'b': 'r9', 'c': 'r10', 'd': 'r11'}
    parts = line.split()
    cmd, args = parts[0], parts[1:]

    code = []
    jump = None
    if cmd == 'cpy':
        s = names.get(args[0], args[0])
        code.append('mov {}, {}'.format(names[args[1]], s))
    elif cmd in {'inc', 'dec'}:
        code.append('{} {}'.format(cmd, names[args[0]]))
    elif cmd == 'jnz':
        jump = ix + int(args[1])
        if args[0] in names:
            code.append('cmp {}, 0'.format(names[args[0]]))
            code.append('jnz l{}'.format(jump))
        elif int(args[0]):
            code.append('jmp l{}'.format(jump))
    return code, jump


def p1(lines, c=0):
    print PREAMBLE.format(c)
    jumps = set()
    source = []
    for ix, line in enumerate(lines):
        code, jump = _code(ix, line)
        source.append(code)
        jumps.add(jump)

    for ix, part in enumerate(source):
        if ix in jumps:
            print 'l{}:'.format(ix)
        for line in part:
            print ' ' * 8 + line

    print PRINTF

p1(sys.stdin, c=1)
