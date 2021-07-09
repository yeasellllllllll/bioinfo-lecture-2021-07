import sys


def rec(l1, l2, n):
    if n < 2:
        return l2
    else:
        ltmp = []
        for s1 in l1:  # A, C, G, T
            for s2 in l2:  # AA, AC, AG, AT, CA, CC, CG, CT, ....
                ltmp.append(s1 + s2)
        return rec(l1, ltmp, n - 1)


l1 = ["A", "C", "G", "T"]
l2 = ["A", "C", "G", "T"]
n = int(sys.argv[1])
l = rec(l1, l2, n)
print(l)
