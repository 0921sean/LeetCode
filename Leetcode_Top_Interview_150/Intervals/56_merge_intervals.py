from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        left, right = intervals[0][0], intervals[0][1]
        result = []

        for interval in intervals:
            if interval[0] <= right:
                right = max(right, interval[1])
            else:
                result.append([left, right])
                left, right = interval[0], interval[1]
        result.append([left, right])

        return result