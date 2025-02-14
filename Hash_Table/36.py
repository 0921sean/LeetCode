from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 가로 중복 체크
        for row in board:
            for i in row:
                if i != '.' and row.count(i) > 1:
                    return False

        # 세로 중복 체크
        for i in range(9):
            col = [row[i] for row in board]
            for j in col:
                if j != '.' and col.count(j) > 1:
                    return False
                
        # 3x3 중복 체크
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                for k in square:
                    if k != '.' and square.count(k) > 1:
                        return False
        return True
    
# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    solution = Solution()
    board_list = [[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]], [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]]
    for board in board_list:
        result = solution.isValidSudoku(board)
        print(result)