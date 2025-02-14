from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        flip_num = 0
        
        for i in range(n):
            if nums[i] == 0:
                if i >= n-2:
                    return -1
                for j in range(i, i+3):
                    nums[j] ^= 1
                flip_num += 1
        return flip_num
         
# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    solution = Solution()
    nums_list = [[0,1,1,1,0,0], [0,1,1,1]]
    for nums in nums_list:
        result = solution.minOperations(nums)
        print(result)