def triangle(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)


def p1(f):
    possible = 0
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = [int(p) for p in line.split()]
        if triangle(*parts):
            possible += 1
    return possible


def p2(f):
    lines = [l.strip() for l in f]
    lines = [map(int, l.split()) for l in lines if l]
    nums = zip(*lines)
    nums = nums[0] + nums[1] + nums[2]
    triangles = zip(*[iter(nums)] * 3)
    possible = sum(triangle(*t) for t in triangles)
    return possible


with open('input_3.txt') as f:
    print p1(f)
    f.seek(0)
    print p2(f)
