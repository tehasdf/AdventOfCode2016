import sys
from collections import Counter

rows = zip(*[l.strip() for l in sys.stdin])
print ''.join(Counter(l).most_common()[-1][0] for l in rows)  # 0 zamiast -1 dla part1
