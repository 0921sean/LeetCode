from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 두 포인터 사용 (List는 이미 정렬된 리스트임을 활용)
        left, right = 0, len(nums) - 1
        result = [0] * len(nums)
        pos = len(nums) - 1

        while left <= right:
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2
            
            if left_square > right_square:
                result[pos] = left_square
                left += 1
            else:
                result[pos] = right_square
                right -= 1
            
            pos -= 1
        
        return result

# O(nlogn) 풀이
# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         sorted_list = []
            
#         for num in nums:
#             square = num ** 2
#             # square가 들어가야 할 인덱스 결정
#             index = 0
#             for i, x in enumerate(sorted_list):
#                 if square > x:
#                     index += 1
                    
#             sorted_list.insert(index, square)
            
#         return sorted_list

# 시간 초과
# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         sorted_list = []
            
#         for num in nums:
#             square = num ** 2
#             # square가 들어가야 할 인덱스 결정
#             index = 0
#             for i, x in enumerate(sorted_list):
#                 if square > x:
#                     index += 1
                    
#             sorted_list.insert(index, square)
            
#         return sorted_list
            
# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    solution = Solution()
    nums_list = [[], [-4], [-4, -1, 0, 3, 10]]
    for nums in nums_list:
        result = solution.sortedSquares(nums)
        print(result)