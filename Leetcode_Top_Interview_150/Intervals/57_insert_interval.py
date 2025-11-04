from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_left, new_right = newInterval[0], newInterval[1]
        new_intervals_added = False
        result = []
        
        for idx, interval in enumerate(intervals):
            left, right = interval[0], interval[1]
            if left < new_left and right < new_left:
                result.append([left, right])
            elif left > new_right and right > new_right:
                result.append([new_left, new_right])
                new_intervals_added = True
                for i in range(idx, len(intervals)):
                    result.append(intervals[i])
                break
            else:
                new_left = min(left, new_left)
                new_right = max(right, new_right)

        if not new_intervals_added:
            result.append([new_left, new_right])
            
        return result