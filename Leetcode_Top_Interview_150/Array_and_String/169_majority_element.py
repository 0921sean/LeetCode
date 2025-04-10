from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element_count = {}
        for num in nums:
            element_count[num] = element_count.get(num, 0) + 1

        for element, count in element_count.items():
            if count > len(nums) / 2:
                return element