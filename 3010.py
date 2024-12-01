from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        min_val = float('inf')
        second_min = float('inf')
        for num in nums[1:]:
            if num <= min_val:
                second_min = min_val
                min_val = num
            elif min_val <= num < second_min:
                second_min = num
        return nums[0] + min_val + second_min