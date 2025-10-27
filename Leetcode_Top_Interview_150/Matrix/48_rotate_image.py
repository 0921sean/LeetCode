from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        new_matrix = [[] for _ in range(len(matrix))]

        for row in reversed(matrix):
            for i, el in enumerate(row):
                new_matrix[i].append(el)
        
        matrix[:] = new_matrix