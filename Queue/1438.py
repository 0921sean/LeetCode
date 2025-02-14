from typing import List

# 당연하지만 Time Limit Exceeded Error
# class Solution:
#     def longestSubarray(self, nums: List[int], limit: int) -> int:
#         # 변수 초기화
#         n = len(nums)
#         result_list = []
        
#         for i in range(n):
#             for j in range(i, n):
#                 split_nums = nums[i:j+1]
#                 if max(split_nums) - min(split_nums) <= limit:
#                     result_list.append(len(split_nums))
#         return max(result_list)

from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # 변수 초기화
        inc = deque()
        dec = deque()
        max_len = 0
        left = 0
        
        for right in range(len(nums)):
            while inc and inc[-1] > nums[right]:
                inc.pop()
            while dec and dec[-1] < nums[right]:
                dec.pop()
            inc.append(nums[right])
            dec.append(nums[right])
            
            while dec[0] - inc[0] > limit:
                if nums[left] == inc[0]:
                    inc.popleft()
                if nums[left] == dec[0]:
                    dec.popleft()
                left += 1
            max_len = max(max_len, right - left + 1)
            
        return max_len
            
# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    solution = Solution()
    nums_list = [[8,2,4,7], [10,1,2,4,7,2], [4,2,2,2,4,4,2,2]]
    limit_list = [4, 5, 0]
    for nums, limit in zip(nums_list, limit_list):
        result = solution.longestSubarray(nums, limit)
        print(result)