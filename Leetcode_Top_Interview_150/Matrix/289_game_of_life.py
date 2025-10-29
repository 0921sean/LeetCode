from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        states = {}

        for r in range(m):
            for c in range(n):
                zeroes, ones, state = 0, 0, None
                
                for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), \
                (0, 1), (1, -1), (1, 0), (1, 1)]:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < m and 0 <= nc < n:
                        if board[nr][nc] == 0:
                            zeroes += 1
                        else:
                            ones += 1
                
                if board[r][c] == 1:
                    if ones < 2:
                        state = 0
                    elif 2 <= ones <= 3:
                        state = 1
                    elif ones > 3:
                        state = 0

                else:
                    if ones == 3:
                        state = 1
                    else:
                        state = 0

                states[(r, c)] = state

        for r in range(m):
            for c in range(n):
                board[r][c] = states[(r, c)]