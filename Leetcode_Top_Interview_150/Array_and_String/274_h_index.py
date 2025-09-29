from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for i in range(len(citations), -1, -1):
            if i == len(citations) and citations[-1] >= i:
                return i
            if citations[i-1] >= i and citations[i] <= i:
                return i
            
# 테스트 케이스
print(Solution().hIndex([3,0,6,1,5]))  # 3
print(Solution().hIndex([1,3,1]))      # 1