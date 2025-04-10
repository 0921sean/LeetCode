from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums[0] == 0 and len(nums) > 1:
            return False

        for i in range(len(nums) - 1):
            if nums[i] == 0:
                isOkay = False
                for j in range(i-1, -1, -1):
                    if nums[j] != 0 and nums[j] > i-j:
                        isOkay = True
                if not isOkay:
                    return False

        return True