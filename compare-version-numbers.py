class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        
        A = A.split('.')
        B = B.split('.')
        
        a = len(A)
        b = len(B)
        
        n = 0
        
        while a < b :
            A.append("0")
            a += 1
        
        while b < a:
            B.append("0")
            b += 1
            
        for i in range(a):
            
            if int(A[n]) > int(B[n]): return 1
            
            elif int(A[n]) < int(B[n]): return -1
            
            
            n += 1
            
        
        return 0
