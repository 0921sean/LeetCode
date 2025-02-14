from typing import List, Optional
import bisect

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    # # __repr__ 메서드 추가
    # def __repr__(self):
    #     return f"TreeNode(val={self.val})"
    
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        stack = [root]
        for value in preorder[1:]:
            if value < stack[-1].val:
                stack[-1].left = TreeNode(value)
                stack.append(stack[-1].left)
            else:
                while stack and stack[-1].val < value:
                    last = stack.pop()
                last.right = TreeNode(value)
                stack.append(last.right)
            # print(stack)
        return root
    
# BFS 함수: 트리를 리스트로 변환
def bfs(root: TreeNode) -> List[Optional[int]]:
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # 마지막에 불필요한 None 제거
    while result and result[-1] is None:
        result.pop()
    
    return result
    
# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    solution = Solution()
    preorder_list = [[8,5,1,7,10,12], [1,3]]
    for preorder in preorder_list:
        result = solution.bstFromPreorder(preorder)
        print(bfs(result))