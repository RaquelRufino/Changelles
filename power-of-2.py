class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):
        
        if int(A) > 1:
            if (int(A) and not(int(A) & (int(A) - 1))): return 1
        
        return 0
