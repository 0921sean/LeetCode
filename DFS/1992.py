from typing import List
from collections import deque

class Solution:
    # DFS
    def findFarmlandByDFS(self, land: List[List[int]]) -> List[List[int]]:
        def dfs(x: int, y: int) -> tuple[int]:
            stack = [(x, y)]
            min_row, min_col = x, y
            max_row, max_col = x, y
            visited.add((x, y))
            
            while stack:
                print("Stack:", stack)
                cur_x, cur_y = stack.pop()
                
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = cur_x + dx, cur_y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and land[nx][ny] == 1:
                        visited.add((nx, ny))
                        stack.append((nx, ny))
                        min_row = min(min_row, nx)
                        min_col = min(min_col, ny)
                        max_row = max(max_row, nx)
                        max_col = max(max_col, ny)
                        
            return (min_row, min_col, max_row, max_col)
        
        rows, cols = len(land), len(land[0])
        visited = set()
        result = []
        
        for i in range(rows):
            for j in range(cols):
                if land[i][j] == 1 and (i, j) not in visited:
                    min_row, min_col, max_row, max_col = dfs(i, j)
                    result.append([min_row, min_col, max_row, max_col])
                    
        return result

    # BFS
    def findFarmlandByBFS(self, land: List[List[int]]) -> List[List[int]]:
        rows, cols = len(land), len(land[0])
        result = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        
        def bfs(start_row: int, start_col: int) -> tuple[int]:
            queue = deque([(start_row, start_col)])
            visited.add((start_row, start_col))
            min_row, min_col, max_row, max_col = start_row, start_col, start_row, start_col
            
            while queue:
                print("Queue:", queue)
                cur_row, cur_col = queue.popleft()

                for dr, dc in directions:
                    new_row, new_col = cur_row + dr, cur_col + dc
                    
                    if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited and land[new_row][new_col] == 1:
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))
                        min_row = min(min_row, new_row)
                        min_col = min(min_col, new_col)
                        max_row = max(max_row, new_row)
                        max_col = max(max_col, new_col)
                        
            return (min_row, min_col, max_row, max_col)
        
        for i in range(rows):
            for j in range(cols):
                if land[i][j] == 1 and (i, j) not in visited:
                    farmland = bfs(i, j)
                    result.append(farmland)
                    
        return result
    
# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    solution = Solution()
    land_list = [[[1,0,0],[0,1,1],[0,1,1]], [[1,1],[1,1]], [[0]], [[1, 1, 1, 0, 1],[1, 1, 1, 0, 1],[1, 1, 1, 1, 0],[0, 0, 1, 1, 0],[1, 0, 0, 0, 1]]]
    for land in land_list:
        resultDFS = solution.findFarmlandByDFS(land)
        resultBFS = solution.findFarmlandByBFS(land)
        print(resultDFS)
        print(resultBFS)