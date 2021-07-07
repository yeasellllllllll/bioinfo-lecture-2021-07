#! /usr/bin/env python

from collections import Counter

toCount = 'We tried list and we tried dicts also we tried Zen'

l_toCount = toCount.split()
cnt = Counter(l_toCount)

print(cnt)
cnt['tried'] += 100
print(cnt)
