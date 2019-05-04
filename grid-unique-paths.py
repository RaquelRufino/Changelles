class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    
        
    def uniquePaths(self, A, B):
        
        count = [[0]] * max(A,B)
        for i in range(max(A,B)):
            count[i].append(0)
          
        
        for i in range(A):
            count[i][0] = 1
        
        for i in range(B):
            count[0][i] = 1
        
        for i in range(1,A):
            for j in range(B):
                
                count[i][j] = count[i - 1][j] + count[i][j-1]
                
            

        return count[A - 1][B - 1]
