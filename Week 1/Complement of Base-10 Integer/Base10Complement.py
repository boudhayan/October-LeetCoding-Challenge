from math import log2


def bitwiseComplement(N):
    if N == 0:
        return 1
    # length of N in binary representation
    length = floor(log2(N)) + 1
    # bitmask has the same length as N and contains only ones 1..1
    bitmask = (1 << length) - 1
    return bitmask ^ N
