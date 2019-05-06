# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
        
        if A is None or B is None:
            return None
        
        a = A
        b = B
        
        while a != b:
            
            if a is None: a = A
            
            else: a = a.next
            
            
            if b is None: b = B
            else: b = b.next
                

        return a
        
        
        
        
        
        
        
        
        
        
        
        
        
