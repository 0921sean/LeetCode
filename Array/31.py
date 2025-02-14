from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        index = -1
        
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                index = i
                break
            
        if index == -1:
            nums.reverse()
            return
        for i in range(n - 1, index, -1):
            if nums[i] > nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
                break
        nums[index + 1:] = reversed(nums[index + 1:])
        
# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    solution = Solution()
    nums_list = [[1,2,3],[3,2,1],[1,1,5]]
    for nums in nums_list:
        solution.nextPermutation(nums)
        print(nums)