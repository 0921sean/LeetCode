from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_list = []
        product_without_zero = 1
        product = 1
        for i in range(len(nums)):
            if nums[i] != 0:
                product_without_zero *= nums[i]
            product *= nums[i]
        for i in range(len(nums)):
            if nums[i] == 0:
                product_list.append(product_without_zero) if nums.count(0) == 1 else product_list.append(0)
            else:
                product_list.append(product // nums[i])

        return product_list

        # # 이런 풀이도 있음
        # output = [1] * len(nums)

        # left = 1
        # for i in range(len(nums)):
        #     output[i] *= left
        #     left *= nums[i]
        
        # right = 1
        # for i in range(len(nums) - 1, -1, -1):
        #     output[i] *= right
        #     right *= nums[i]

        # return output