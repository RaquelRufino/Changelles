# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):

        
        if A is None: return B
        
        if B is None: return A
        
        s = t = ListNode('root')
        
        while not (A is None or B is None):
            
            
            if A.val < B.val:
                
                c = A
                
                A = A.next
            
            else :
                
                c = B
                
                B = B.next
            
            
            t.next = c
            
            t = t.next
        
        
        t.next = A or B
        
        return s.next
                
