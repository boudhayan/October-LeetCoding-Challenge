
# Greedy Approach
# Time Complexity: O(nlogn)
# Space Complexity: O(1)

def removeCoveredIntervals(intervals):
    # sort ny the starting point of the interval and incase two staring points are equal, place the interval with
    # longer distance/interval infront
    intervals.sort(key=lambda x: (x[0], -x[1]))
    # first interval will always be not covered as the list is sorted now
    count = 0
    previous_end = 0
    for _, end in intervals:
        if previous_end < end:
            count += 1
            previous_end = end
    return count


print(removeCoveredIntervals([[1, 4], [3, 6], [2, 8]]))
