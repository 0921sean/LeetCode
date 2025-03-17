from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = []
        tmp = None
        
        for num in nums:
            if tmp == None:
                result.append(num)
            else:
                if num != tmp:
                    result.append(num)
            tmp = num
        
        nums[:] = result
        return len(result)
    
# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    solution = Solution()
    nums_list = [[1,1,2], [0,0,1,1,1,2,2,3,3,4], [1,1,1,1,1,1,1,1,1,1]]
    for nums in nums_list:
        result = solution.removeDuplicates(nums)
        print(result)