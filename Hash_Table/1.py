from typing import List

# 시간복잡도 O(n) 풀이
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in complement_dict:
                return [complement_dict[complement], i]
            complement_dict[num] = i

# 시간복잡도 O(n^2) 풀이
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(0, len(nums)-1):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
                
# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    solution = Solution()
    nums_list = [[2, 7, 11, 15], [3, 2, 4], [3, 3]]
    target_list = [9, 6, 6]
    for nums, target in zip(nums_list, target_list):
        result = solution.twoSum(nums, target)
        print(result)