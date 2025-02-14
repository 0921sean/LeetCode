from typing import List

# # Time Limit Exceeded Error
# class Solution:
#     def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
#         even_pos = []
#         result = []
        
#         for x, num in enumerate(nums):
#             if num % 2 == 0:
#                 even_pos.append(x)
                
#         for query in queries:
#             nums[query[1]] += query[0]
#             if nums[query[1]] % 2 == 0:
#                 if query[1] not in even_pos:
#                     even_pos.append(query[1])
#             else:
#                 if query[1] in even_pos:
#                     even_pos.remove(query[1])
            
#             result.append(sum([nums[i] for i in even_pos]))
            
#         return result
    
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = 0
        result = []
        
        for num in nums:
            if num % 2 == 0:
                even_sum += num
                
        for query in queries:
            val, idx = query
            if nums[idx] % 2 == 0:
                even_sum -= nums[idx]
            nums[idx] += val
            if nums[idx] % 2 == 0:
                even_sum += nums[idx]
            result.append(even_sum)
            
        return result
    
# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    solution = Solution()
    nums_list = [[1,2,3,4],[1]]
    queries_list = [[[1,0],[-3,1],[-4,0],[2,3]],[[4,0]]]
    for nums, queries in zip(nums_list, queries_list):
        result = solution.sumEvenAfterQueries(nums, queries)
        print(result)