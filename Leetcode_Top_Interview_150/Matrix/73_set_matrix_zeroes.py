from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_row = set()
        zero_col = set()

        for i, row in enumerate(matrix):
            for j, el in enumerate(row):
                if el == 0:
                    zero_row.add(i)
                    zero_col.add(j)

        for i in zero_row:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0

        for j in zero_col:
            for i in range(len(matrix)):
                matrix[i][j] = 0