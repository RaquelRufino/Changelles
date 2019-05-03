class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        

        if A <= 1 : return 1

        for i in range(2,int(A ** 0.5) + 1):
            
            p = i
            
            while p < A:
                
                p *= i
                
                if p == A:
                    return 1
        
        
        return 0
                    
