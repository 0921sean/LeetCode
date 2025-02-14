from typing import List

# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         res = []
        
#         def dfs(openP, closeP, s):
#             if openP == closeP and openP + closeP == 2 * n:
#                 res.append(s)
#                 return
            
#             if openP < n:
#                 dfs(openP + 1, closeP, s + '(')
            
#             if closeP < openP:
#                 dfs(openP, closeP + 1, s + ')')
                
#         dfs(0, 0, "")
        
#         return res
    
# 더 빠름
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(l: int, r: int, s: list[str]) -> None:
            if l == 0 and r == 0:
                res.append("".join(s))
            if l > 0:
                s.append('(')
                dfs(l - 1, r, s)
                s.pop()
            if l < r:
                s.append(')')
                dfs(l, r - 1, s)
                s.pop()
            
        dfs(n, n, [])
        return res
    
# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    solution = Solution()
    n_list = [1,2,3,4]
    for n in n_list:
        result = solution.generateParenthesis(n)
        print(result)