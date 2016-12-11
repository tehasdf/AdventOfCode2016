import hashlib
# import itertools


# def letters(inp):
#     i = 0
#     b = hashlib.md5(inp)
#     while True:
#         h = b.copy().update(str(i)).digest()
#         # h = hashlib.md5(inp + str(i)).digest()
#         if h[0] == '\x00' and h[1] == '\x00' and h[2] < '\x10':
#             yield h[5]
#         i += 1


# def password(inp):
#     return ''.join(itertools.islice(letters(inp), 8))


# def letters_pos(inp):
#     i = 0
#     b = hashlib.md5(inp)
#     while True:
#         h = b.copy()
#         h.update(str(i))
#         h = h.digest()
#         # h = hashlib.md5('{0}{1}'.format(inp, i)).hexdigest()
#         # if h.startswith('00000'):
#         if h[:2] == '\x00\x00' and h[2] < '\x10':
#             h = h.encode('hex')
#             print int(h[5], 16), h[6], h
#             yield int(h[5], 16), h[6]
#         i += 1


# def password2(inp):
#     pwd = {}
#     for pos, c in letters_pos(inp):
#         if pos < 8 and pos not in pwd:
#             pwd[pos] = c
#             print ''.join(pwd.get(i, '_') for i in range(8))
#             if len(pwd) == 8:
#                 break
#     return ''.join(pwd.get(i, '_') for i in range(8))


def password3(inp, md5=hashlib.md5, ord=ord, str=str):
    out = [None] * 8
    got = 0
    for i in range(999999999):
        h = md5(inp + str(i)).digest()
        if h < '\x00\x00\x08':
            pos = ord(h[2])
            if out[pos] is None:
                out[pos] = h[3].encode('hex')[0]
                got += 1
                if got == 8:
                    break
    return ''.join(out)

# assert password('abc') == '18f47a30'
# print password('reyedfim')

# assert password2('abc') == '05ace8e3'

# import dis
# dis.dis(password3)
print(password3(b'reyedfim'))
