from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        cnt = 0
        candies = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(n - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                candies[i - 1] = max(candies[i] + 1, candies[i - 1])
            cnt += candies[i - 1]
        return cnt + candies[n - 1]

        # # [20000, 19999, ..., 1]인 케이스에서 시간초과
        # prev, curr, left, right = ratings[0], 0, 0, 0
        # candy_list = [1]
    
        # for right in range(1, len(ratings)):
        #     curr = ratings[right]
        #     if curr < prev:
        #         for i in range(right - 1, left - 1, -1):
        #             if candy_list[i] < right - i + 1:
        #                 candy_list[i] = right - i + 1
        #             else:
        #                 break
        #             # candy_list[i] = max(candy_list[i], right - i + 1)
        #         candy_list.append(1)
        #     if curr > prev:
        #         candy_list.append(candy_list[right - 1] + 1)
        #         left = right
        #     if curr == prev:
        #         candy_list.append(1)
        #         left = right
        #     prev = curr
        # return sum(candy_list)