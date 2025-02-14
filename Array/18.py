from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        result = []
        
        nums.sort()
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1, n):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                
                k = j + 1
                l = n - 1
                
                while k < l:
                    print(i, j, k, l)
                    total = nums[i] + nums[j] + nums[k] + nums[l]
                    if total > target:
                        l -= 1
                    elif total < target:
                        k += 1
                    else:
                        result.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        while nums[k] == nums[k-1] and k < l:
                            k += 1
                        
        return result
    
# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    solution = Solution()
    nums_list = [[1, 0, -1, 0, -2, 2], [2, 2, 2, 2, 2], [-3,-2,-1,0,0,1,2,3]]
    target_list = [0, 8, 0]
    for nums, target in zip(nums_list, target_list):
        result = solution.fourSum(nums, target)
        print(result)