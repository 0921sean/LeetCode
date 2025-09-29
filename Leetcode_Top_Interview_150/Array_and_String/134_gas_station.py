from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        fill_list = list(gas[i] - cost[i] for i in range(len(gas))) # 각 주유소에서의 gas - cost
        
        # filling = [-2, -2, -2, 3, 3] / sum_list = [-2, -4, -6, -3, 0]
        sum_list = []
        summed = 0
        for i in range(len(fill_list)):
            summed += fill_list[i]
            sum_list.append(summed)

        min_sum = min(sum_list)
        for i in range(len(gas) - 1, -1, -1):
            if sum_list[i] == min_sum:
                return i + 1 if i != len(gas) - 1 else 0

        # 아래 풀이도 가능함 (내가 풀음)
        # for i in range(len(gas)):
        #     if i == 0 and travel[i] >= 0:
        #         filled = 0
        #         idx = i
        #         while filled >= 0:
        #             filled += travel[idx]
        #             idx += 1
        #             if idx == len(gas):
        #                 return i
        #         continue
        #     if travel[i] > 0 and travel[i-1] < 0:
        #         filled = 0
        #         idx = i
        #         while filled >= 0:
        #             filled += travel[idx]
        #             if idx == len(gas) - 1:
        #                 idx = 0
        #             else:
        #                 idx += 1
        #             if idx == i:
        #                 return i
        #         continue