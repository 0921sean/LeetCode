from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0

        while left < right:
            # 둘 중 더 작은 값을 움직이는 이유는
            # 더 큰 값을 갖고 있는 인덱스는 이미 현재 가장 긴 바에 대한 정보를 갖고 있는 것이니까
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]

        return water