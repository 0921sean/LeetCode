from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        checked = {}

        for i, num in enumerate(nums):
            if num in checked:
                if i - checked[num] <= k:
                    return True
            checked[num] = i
        
        return False