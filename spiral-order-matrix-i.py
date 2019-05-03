class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        m = len(A)
        n = len(A[0])
        t = 0
        b = m - 1
        l = 0
        r = n - 1
        dir = 0
        result = []
        
        while t <= b and l <= r:
            
            if dir == 0 :
                
                for i in A[t][l:r + 1]:
                    result.append(i)
                
                dir += 1
                t += 1
                
            elif dir == 1:
                
                for i in A[t:b + 1]:
                    
                    result.append(i[r])
                
                dir += 1
                r -= 1
            
            elif dir == 2 :
                
                for i in A[b][l:r + 1][::-1]:
                    
                    result.append(i)
                
                dir += 1
                b -= 1
            
            elif dir == 3:
                
                for i in A[t:b + 1][::-1]:
                    
                    result.append(i[l])
                
                dir = 0
                l += 1
                
            
            
        return result
