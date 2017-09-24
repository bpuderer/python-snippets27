import re
from collections import Counter


def pair_sum_to_value(seq, value):
    """"test if any pair in sequence sum to value"""
    for i in xrange(len(seq)):
        for j in xrange(i+1, len(seq)):
            if seq[i]+seq[j] == value:
                return True
    return False


def is_mirror_number(i):
    tmp = str(i)
    if tmp == tmp[::-1]:
        return True
    return False


def token_counter():
    cnt = Counter()
    lines = ['text text [pass] [error] [pass] pass [fail] text', '[fail] [pass] [pass...']
    for line in lines:
        # [TOKEN]
        tokens = re.findall('\[(.+?)\]', line)
        for token in tokens:
            cnt[token] += 1
    print dict(cnt)


if __name__ == "__main__":

    print pair_sum_to_value([], 0)
    print pair_sum_to_value([1], 0)
    print pair_sum_to_value([1], 1)
    print pair_sum_to_value([1], 2)
    print pair_sum_to_value([1, 2], 3)
    print pair_sum_to_value([2, 9, 3], 18)
    print pair_sum_to_value([1, 4, 6, 7, 5, 9, 7], 16)
    print pair_sum_to_value([1, 4, 6, 7, 5, 9, 7], 17)

    print '******'

    print is_mirror_number(12321)
    print is_mirror_number(1232)

    print '******'

    token_counter()
