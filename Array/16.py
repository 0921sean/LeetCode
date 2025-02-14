from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        result = []
        min_dif = float('inf')
        
        nums.sort()
        
        for i in range(n):
            j = i + 1
            k = n - 1
            
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                # print(nums[i], nums[j], nums[k], total)
                if total > target:
                    k -= 1
                elif total < target:
                    j += 1
                else:
                    return total
                dif = abs(total - target)
                if dif < min_dif:
                    min_dif = dif
                    result.append(total)
                    # print(result)
                    
        return result[-1]
        
# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    solution = Solution()
    nums_list = [[-1, 2, 1, -4], [0, 0, 0], [1, 1, 1, 0], [1, 1, 1, 0, 0]]
    target_list = [1, 1, -100, 100]
    for nums, target in zip(nums_list, target_list):
        result = solution.threeSumClosest(nums, target)
        print(result)