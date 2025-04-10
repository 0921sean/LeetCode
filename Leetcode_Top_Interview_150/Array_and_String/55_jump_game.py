from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 도달할 수 있는 가장 먼 위치
        max_reach = 0
        
        for i in range(len(nums)):
            # 현재 위치가 도달할 수 있는 최대 거리보다 크면 도달 불가능
            if i > max_reach:
                return False
            
            # 현재 위치에서 점프하여 도달할 수 있는 최대 거리 업데이트
            max_reach = max(max_reach, i + nums[i])
            
            # 이미 마지막 인덱스에 도달할 수 있다면 더 이상 확인할 필요 없음
            if max_reach >= len(nums) - 1:
                return True
            
        return False
        
        # if nums[0] == 0 and len(nums) > 1:
        #     return False

        # for i in range(len(nums) - 1):
        #     if nums[i] == 0:
        #         isOkay = False
        #         for j in range(i-1, -1, -1):
        #             if nums[j] != 0 and nums[j] > i-j:
        #                 isOkay = True
        #         if not isOkay:
        #             return False

        # return True