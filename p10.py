import re


def p1(inp):
    bots = {}
    plan = {}
    for line in inp:
        if line.startswith('value'):
            val, bot = re.findall('bot \d+|\d+', line)
            bots.setdefault(bot, []).append(int(val))
        elif line.startswith('bot'):
            source, low, high = re.findall('\w+ \d+', line)
            plan[source] = (low, high)

    while plan:
        ready = [k for k, v in bots.items() if len(v) == 2]
        for r in ready:
            chips = bots.pop(r)
            target_low, target_high = plan.pop(r)
            bots.setdefault(target_low, []).append(min(chips))
            bots.setdefault(target_high, []).append(max(chips))

    return bots


with open('input_10.txt') as f:
    out = p1(f)
print out['output 0'][0] * out['output 1'][0] * out['output 2'][0]
