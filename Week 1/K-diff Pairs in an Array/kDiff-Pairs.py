from collections import Counter

"""
    Time Complexity: O(n)
    Space Complexity: O(n)
"""


def findPairs(nums, k):
    hashmap = Counter(nums)
    if k >= 1:
        res = sum([a + k in hashmap for a in hashmap])
    else:
        res = sum([hashmap[a] > 1 for a in hashmap])
    return res


print(findPairs([1, 3, 1, 5, 4], 0))
