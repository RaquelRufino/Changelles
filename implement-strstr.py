class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B):
        
        n = 0
        x = len(A)
        y = len(B)
        for i in A:
            
            if i == B[0] and (x - n + 1)  >= y :
                
                if A[n: n + y] == B : return n  
            
                
            n += 1
        
        return -1
