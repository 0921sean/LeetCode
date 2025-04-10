from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        # 현재 위치, 가능한 최대 위치, 점프 횟수
        pos, max_pos, num_jump = 0, nums[0], 1

        while max_pos < len(nums) - 1:
            num_jump += 1
            for i in range(pos + 1, min(max_pos + 1, len(nums))):
                max_pos = max(max_pos, nums[i] + i)
                pos = i

        return num_jump