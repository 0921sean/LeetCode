from typing import Optional, List

# # Time complexity: O(n^2) => Time Limit Exceeded Error 
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode(0)
#         dummy.next = head
#         current = dummy
        
#         while current.next:
#             runner = current.next.next
#             must_remove = False
            
#             while runner:
#                 if runner.val > current.next.val:
#                     must_remove = True
#                     break
#                 runner = runner.next
            
#             if must_remove:
#                 current.next = current.next.next
#             else:
#                 current = current.next
                
#         return dummy.next

# # 1. Stack (Time complexity: O(n))
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         stack = []
#         current = head
        
#         while current:
#             while stack and stack[-1] < current.val:
#                 stack.pop()
#             stack.append(current.val)
#             current = current.next
            
#         dummy = ListNode(0)
#         current = dummy
#         for val in stack:
#             current.next = ListNode(val)
#             current = current.next
            
#         return dummy.next

# 2: Recursion (Time complexity: O(n))
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         # If linked list is empty of has only one node
#         if head is None or head.next is None:
#             return head
            
#         next_node = self.removeNodes(head.next)
            
#         # If next node has greater value than head, delete the head
#         if head.val < next_node.val:
#             return next_node
          
#         # Otherwise, keep the head  
#         head.next = next_node
#         return head
    
# 3: Reverse Twice (Time complexity: O(n))
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverse_list(self, head):
        prev = None
        current = head
        next_temp = None
        
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
            
        return prev
            
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverse_list(head)
            
        maximum = 0
        prev = None
        current = head
        
        while current:
            maximum = max(maximum, current.val)
            
            if current.val < maximum:
                prev.next = current.next
                current = current.next
            else:
                prev = current
                current = current.next
        
        return self.reverse_list(head)
    
# Helper 함수: 리스트를 링크드 리스트로 변환
def list_to_linked_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Helper 함수: 링크드 리스트를 리스트로 변환
def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result
    
# 실행 예제
if __name__ == "__main__":
    # 링크드 리스트 생성
    head_list = [[5,2,13,3,8], [1,1,1,1]]
    solution = Solution()
    for head in head_list:
        head = list_to_linked_list(head)
        result = solution.removeNodes(head)
        print(linked_list_to_list(result))