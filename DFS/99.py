from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder_traversal(node):
            if not node:
                return []
            return inorder_traversal(node.left) + [node] + inorder_traversal(node.right)
        
        nodes = inorder_traversal(root)
        
        first, second = None, None
        for i in range(len(nodes)-1):
            if nodes[i].val > nodes[i + 1].val:
                if not first:
                    first = nodes[i]
                second = nodes[i + 1]
        
        # Actually swap the values (this was missing)
        first.val, second.val = second.val, first.val

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

# Function to convert BST back to list (level order) for verification
def bst_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left if node.left else None)
            queue.append(node.right if node.right else None)
        else:
            result.append(None)
    
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    
    return result

# Function to verify the BST property
def is_valid_bst(root: Optional[TreeNode]) -> bool:
    def inorder(node):
        if not node:
            return []
        return inorder(node.left) + [node.val] + inorder(node.right)
    
    values = inorder(root)
    return all(values[i] < values[i+1] for i in range(len(values)-1))

# Main function for testing
if __name__ == "__main__":
    solution = Solution()
    root_list = [[1, 3, None, None, 2], [3, 1, 4, None, None, 2]]
    
    for lst in root_list:
        root = list_to_bst(lst)
        solution.recoverTree(root)
        print(bst_to_list(root))