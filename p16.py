a = '10011111011011001'
d = 272
d = 35651584
while len(a) < d:
    a = a + '0' + ''.join('1' if x == '0' else '0' for x in a[::-1])

a = a[:d]
checksum = a
while True:
    checksum = ''.join('1' if a == b else '0'
                       for a, b in zip(checksum[::2], checksum[1::2]))
    if len(checksum) % 2 == 1:
        break

print checksum
