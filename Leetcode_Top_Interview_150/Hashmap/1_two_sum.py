from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # index와 target을 이루기 위해 필요한 수를 저장하는 딕셔너리
        complement_dict = {}
        
        for i in range(len(nums)):
            num = nums[i]
            if num in complement_dict.keys():
                return [complement_dict[num], i]
            complement_dict[target - num] = i