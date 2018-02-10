from datetime import datetime
from collections import namedtuple


# https://stackoverflow.com/a/9044111
# User: Raymond Hettinger
# https://stackoverflow.com/users/1001643/raymond-hettinger
Range = namedtuple('Range', ['start', 'end'])

def overlap_days(r1, r2):
    latest_start = max(r1.start, r2.start)
    earliest_end = min(r1.end, r2.end)
    delta = (earliest_end - latest_start).days + 1
    overlap = max(0, delta)
    return overlap
