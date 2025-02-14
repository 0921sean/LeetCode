from typing import List

# # Time Limit Exceeded Error
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         n = len(nums)
#         result = set()
        
#         for i in range(n):
#             for j in range(i+1, n):
#                 if (0 - nums[i] - nums[j]) in nums[j+1:]:
#                     result.add(tuple(sorted([nums[i], nums[j], 0 - nums[i] - nums[j]])))
#         return list(map(list, result))
    
# # 단서 발견
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         # 변수 초기화
#         n = len(nums)
#         result = set()
        
#         nums.sort() # nums 정렬
        
#         for i in range(n-1):
#             if nums[i] * nums[i+1] <= 0:
#                 neg, pos = i, i+1
#                 break
#             if i == n-2:
#                 return []
        
#         for i in range(neg, -1, -1):
#             for j in range(pos, n):
#                 for k in range(j+1, n):
#                     if j != k:
#                         if nums[i] + nums[j] + nums[k] == 0:
#                             result.add(tuple([nums[i], nums[j], nums[k]]))
                            
#         for i in range(pos, n):
#             for j in range(neg, -1, -1):
#                 for k in range(j-1, -1, -1):
#                     if j != k:
#                         if nums[i] + nums[j] + nums[k] == 0:
#                             result.add(tuple([nums[k], nums[j], nums[i]]))
                        
#         return list(map(list, result))
    
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 변수 초기화
        n = len(nums)
        result = []
        
        nums.sort() # nums 정렬
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:  # 중복된 값 건너뛰기
                continue
            
            j = i + 1
            k = n - 1
            
            while j < k:
                cal = nums[i] + nums[j] + nums[k]
                
                if cal > 0:
                    k -= 1
                elif cal < 0:
                    j += 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    
                    while nums[j] == nums[j-1] and j < k:   # 중복된 값 건너뛰기
                        j += 1
                        
        return result
    
# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    solution = Solution()
    nums_list = [[-1, 0, 1, 2, -1, -4], [0, 1, 1], [0, 0, 0], [1,1,1]]
    for nums in nums_list:
        result = solution.threeSum(nums)
        print(result)