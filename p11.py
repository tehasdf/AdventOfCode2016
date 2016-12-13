from itertools import combinations


PART_1 = (
    frozenset({('chip', 'th'), ('gen', 'th'), ('gen', 'pl'), ('gen', 'sr')}),
    frozenset({('chip', 'pl'), ('chip', 'sr')}),
    frozenset({('gen', 'pr'), ('chip', 'pr'), ('gen', 'ru'), ('chip', 'ru')}),
    frozenset()
)
ADDITIONAL = {('gen', 'el'), ('chip', 'el'), ('gen', 'di'), ('chip', 'di')}
PART_2 = tuple([PART_1[0] | ADDITIONAL] + list(PART_1[1:]))


FLOOR_MAP = [[1], [0, 2], [1, 3], [2]]
SEEN = set()


def nextstates(state, floor_map=FLOOR_MAP):
    current_floor, floors = state
    items = floors[current_floor]
    fits_in_elevator = [{i} for i in items] + \
                       [set(x) for x in combinations(items, 2)]

    ret = []
    for what_to_take in fits_in_elevator:
        old_floor = frozenset(items - what_to_take)
        if not possible(old_floor):
            continue

        for where_to_go in floor_map[current_floor]:
            new_floor = frozenset(floors[where_to_go] | what_to_take)
            if not possible(new_floor):
                continue

            newfloors = list(floors)
            newfloors[where_to_go] = new_floor
            newfloors[current_floor] = old_floor
            newfloors = tuple(newfloors)

            newstate = (where_to_go, newfloors)
            h = hash(newstate)
            if h not in SEEN:
                SEEN.add(h)
                ret.append(newstate)
    return ret


def possible(items, cache={}):
    h = hash(items)
    if h not in cache:
        generators = set()
        microchips = set()
        for t, i in items:
            if t == 'gen':
                generators.add(i)
            else:
                microchips.add(i)
        cache[h] = not generators or not microchips \
            or not microchips - generators
    return cache[h]


def p1(start_floors):
    total_items = sum(len(f) for f in start_floors)
    states = [(0, start_floors)]
    i = 0
    while True:
        i += 1
        newstates = []
        for state in states:
            for nextstate in nextstates(state):
                if len(nextstate[1][3]) == total_items:
                    return i, nextstate
                newstates.append(nextstate)
        states = newstates
        print i, len(states)

print p1(PART_1)
