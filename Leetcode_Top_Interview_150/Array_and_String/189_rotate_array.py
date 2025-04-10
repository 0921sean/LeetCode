from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]

# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         k = k % len(nums)
#         result = []

#         for i in range(len(nums)-k, len(nums)):
#             result.append(nums[i])

#         for j in range(len(nums)-k):
#             result.append(nums[j])

#         for k in range(len(result)):
#             nums[k] = result[k]