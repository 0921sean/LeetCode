from typing import List
import copy

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def dfs(x: int, y: int, idx: int) -> bool:
            if idx == len(word):
                return True
            
            if x < 0 or x >= rows or y < 0 or y >= cols or board[x][y] != word[idx]:
                return False
            
            temp, board[x][y] = board[x][y], "#"    # 방문 처리 (백트래킹))
            
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if dfs(x + dx, y + dy, idx + 1):
                    return True
                
            board[x][y] = temp  # 백트래킹 (원상 복구)
            return False
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
                    
        return False
    
# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    solution = Solution()
    board_original = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word_list = ["ABCCED", "SEE", "ABCB"]
    
    for word in word_list:
        board = copy.deepcopy(board_original)
        result = solution.exist(board, word)
        print(result)