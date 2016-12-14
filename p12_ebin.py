# python 2 only - python 3 is not turing-complete, of course

import dis
import sys
import struct
import types


REGISTERS = {'a': 0, 'b': 1, 'c': 2, 'd': 3}


def op(name):
    return chr(dis.opmap[name])


class Compiler(object):
    def __init__(self):
        self.names = ['a', 'b', 'c', 'd']
        self.constants = []
        self.opcodes = []

    def read(self, lines):
        for line in lines:
            line = line.strip()
            if not line:
                continue

            parts = line.split()
            cmd = parts[0]
            count, code = getattr(self, 'handle_{0}'.format(cmd))(*parts[1:])
            self.opcodes.append((count, code))

    def handle_inc(self, reg):
        c = ''.join([
            self.load_global(reg),
            self.load_const(1),
            chr(dis.opmap['INPLACE_ADD']),
            self.store_global(reg)
        ])
        return len(c), lambda _: c

    def handle_dec(self, reg):
        c = ''.join([
            self.load_global(reg),
            self.load_const(1),
            chr(dis.opmap['INPLACE_SUBTRACT']),
            self.store_global(reg)
        ])
        return len(c), lambda _: c

    def handle_cpy(self, source, target):
        parts = []
        if source in self.names:
            parts.append(self.load_global(source))
        else:
            parts.append(self.load_const(int(source)))
        parts.append(self.store_global(target))
        c = ''.join(parts)
        return len(c), lambda _: c

    def handle_jnz(self, check, where):
        where = int(where)
        parts = []
        if check in self.names:
            parts.append(self.load_global(check))
        else:
            parts.append(self.load_const(int(check)))
        parts.append(op('POP_JUMP_IF_TRUE'))
        c = ''.join(parts)

        def _do_jmp(ix):
            target_ix = ix + where
            total = 0
            for i in range(target_ix):
                total += self.opcodes[i][0]

            return c + struct.pack('<H', total)

        return len(c) + 2, _do_jmp

    def finish(self):
        c = self.load_const(None) + 'S'
        self.opcodes.append((len(c), lambda _: c))

    def compile(self):
        rendered = []
        lnotab = []
        for ix, (count, code) in enumerate(self.opcodes):
            lnotab.append(chr(count) + '\x01')
            rendered.append(code(ix))
        codestring = ''.join(rendered)
        c = types.CodeType(
            0,  # argcount
            0,  # nlocals
            1,  # stacksize
            0,  # flags
            codestring,  # codestring
            tuple(self.constants),  # constants
            tuple(self.names),  # names
            (),  # varnames
            '<string>',  # filename
            'tis100',  # name
            0,  # firstlineno
            ''.join(lnotab)  # lnotab
        )
        return c

    def _get_name(self, name):
        try:
            return self.names.index(name)
        except ValueError:
            self.names.append(name)
            return len(self.names) - 1

    def _get_constant(self, name):
        try:
            return self.constants.index(name)
        except ValueError:
            self.constants.append(name)
            return len(self.constants) - 1

    def load_global(self, name):
        return op('LOAD_GLOBAL') + struct.pack('<H', self._get_name(name))

    def store_global(self, name):
        return op('STORE_GLOBAL') + struct.pack('<H', self._get_name(name))

    def load_const(self, const):
        return op('LOAD_CONST') + struct.pack('<H', self._get_constant(const))


def p1(inp):
    compiler = Compiler()
    compiler.read(inp)
    compiler.finish()
    c = compiler.compile()
    dis.dis(c)

    globs, locs = dict.fromkeys('abcd', 0), {}
    exec c in globs, locs
    globs.pop('__builtins__')
    return globs


print p1(sys.stdin)
