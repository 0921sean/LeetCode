from typing import List
from collections import deque

class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        # 변수 초기화
        n = len(prices)
        dp = [0] * (n+1) # dp[i]: i번째 날까지의 최소 가격
        q = deque() # 다음 dp 계산 시 고려해야 할 인덱스
        
        for i in range(n):
            # 해당 dp가 free로 받을 수 있는 경우를 벗어나면 고려할 인덱스 리스트에서 삭제
            while q and (q[0] + 1) * 2 < i + 1:
                q.popleft()
            # 현재 dp가 최소 가격이 되도록 하는 인덱스 리스트에서 불필요한 인덱스 삭제
            while q and dp[q[-1]] + prices[q[-1]] >= dp[i] + prices[i]:
                q.pop()
            q.append(i)
            dp[i + 1] = dp[q[0]] + prices[q[0]]
        
        return dp[n]
    
# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    solution = Solution()
    prices_list = [[3,1,2], [1,10,1,1], [26,18,6,12,49,7,45,45]]
    for prices in prices_list:
        result = solution.minimumCoins(prices)
        print(result)