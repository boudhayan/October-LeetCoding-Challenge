
class Solution(object):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def maximumDistance(self, arrays):
        # initialize distance as 0, current min and current max using first array from 2d array
        distance = 0
        cMin = arrays[0][0]
        cMax = arrays[0][len(arrays[0]) - 1]
        for i in range(1, len(arrays)):
            # comapare and assign max distance to distance by calculating distances from current min and max to current array min and max
            distance = max(distance, abs(
                cMax - arrays[i][0]), abs(arrays[i][len(arrays[i]) - 1] - cMin))
            # check and update current min and max for current array if applicable
            cMin = min(cMin, arrays[i][0])
            cMax = max(cMax, arrays[i][len(arrays[i]) - 1])
        return distance
