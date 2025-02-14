from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # 왼쪽 끝이 빈자리인 경우 (마지막 i는 빈자리가 아닌 왼쪽 끝)
        i = 0
        left_cnt = 0
        while seats[i] == 0:
            left_cnt += 1
            i += 1
        # 오른쪽 끝이 빈자리인 경우 (마지막 j는 빈자리가 아닌 오른쪽 끝)
        j = len(seats)-1
        right_cnt = 0
        while seats[j] == 0:
            right_cnt += 1
            j -= 1
        # 중간 빈자리 계산
        max_cnt = 0
        cnt = 0
        for k in range(i, j+1):
            if seats[k] == 0:
                cnt += 1
            else:
                if cnt > max_cnt:
                    max_cnt = cnt
                cnt = 0
        return max(left_cnt, right_cnt, (max_cnt+1)//2)

# 실행 및 검증
if __name__ == "__main__":
    solution = Solution()
    
    # 테스트 케이스
    test_cases = [
        [1, 0, 0, 0, 1, 0, 1],    # 예상 결과: 2
        [1, 0, 0, 0],             # 예상 결과: 3
        [0, 1],                   # 예상 결과: 1
        [0, 0, 1, 0, 0, 0, 1, 0], # 예상 결과: 3
        [1, 0, 1],                # 예상 결과: 1
        [1,1,1,0,1,0,1,1,0,0,1]   # 예상 결과: 1
    ]
    
    for seats in test_cases:
        print(f"Input: {seats}, Output: {solution.maxDistToClosest(seats)}")