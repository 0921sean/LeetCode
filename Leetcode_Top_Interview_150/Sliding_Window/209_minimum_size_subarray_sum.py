from typing import List
from math import inf

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        total = nums[0]
        min_length = float(inf)

        while True:
            if total >= target: # sum이 target보다 크거나 같다 => length에 추가
                min_length = min(min_length, right - left + 1)
                total -= nums[left]
                left += 1
            else:
                right += 1
                if right >= len(nums):
                    break
                total += nums[right]

        if min_length == float(inf):
            return 0

        return min_length