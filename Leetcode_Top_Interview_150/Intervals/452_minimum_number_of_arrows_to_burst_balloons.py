from typing import List
from math import inf

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        arrow = float(-inf)
        num_arrows = 0
        points.sort(key=lambda x: x[1])

        for point in points:
            if arrow < point[0]:
                arrow = point[1]
                num_arrows += 1

        return num_arrows