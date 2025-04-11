from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left <= right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return left+1, right+1
        
        # comp_dict = {}
        # for i, number in enumerate(numbers):
        #     for idx, comp in comp_dict.items():
        #         if number == comp:
        #             return idx + 1, i + 1
        #     comp_dict[i] = target - number