from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        result = []
        
        for i in range(n):
            if nums[i] != val:
                result.append(nums[i])
                
        len_result = len(result)
        for i in range(len_result):
            nums[i] = result[i]
        for i in range(len_result, n):
            nums[i] = '_'
        return len_result
    
# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    solution = Solution()
    nums_list = [[3,2,2,3], [0,1,2,2,3,0,4,2], [0,1,2,2,3,0,4,2]]
    val_list = [3, 2, 0]
    for nums, val in zip(nums_list, val_list):
        result = solution.removeElement(nums, val)
        print(result)