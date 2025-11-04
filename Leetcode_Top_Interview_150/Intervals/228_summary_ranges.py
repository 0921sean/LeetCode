from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        left, right = 0, 0
        ranges = []

        if len(nums) == 0:
            return []
        
        while right < len(nums):
            if nums[right] - nums[left] == right - left:
                right += 1
            else:
                ranges.append(str(nums[left])) if left == right-1 else ranges.append(str(nums[left]) + "->" + str(nums[right-1]))
                left = right

        ranges.append(str(nums[left])) if left == right-1 else ranges.append(str(nums[left]) + "->" + str(nums[right-1]))

        return ranges