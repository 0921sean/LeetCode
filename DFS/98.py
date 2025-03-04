from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, minimum, maximum):
            # print("({}, {}, {})".format(node, minimum, maximum))
            if not node:
                return True
            
            if not (node.val > minimum and node.val < maximum):
                return False
            
            return valid(node.left, minimum, node.val) and valid(node.right, node.val, maximum)
        
        return valid(root, float('-inf'), float('inf'))
    
def list_to_bst(lst: List[Optional[int]]) -> Optional[TreeNode]:
    if not lst:
        return None
    
    root = TreeNode(lst[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(lst):
        node = queue.popleft()
        
        if i < len(lst) and lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1
        
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1
        
    return root
    
# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    solution = Solution()
    root_list = [[2, 1, 3], [5, 1, 4, None, None, 3, 6]]
    
    for lst in root_list:
        root = list_to_bst(lst)
        result = solution.isValidBST(root)
        print(result)