class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):

        result = 0
        x = len(A) 
        n = 0
        while n < x :
            
            if n < x and A[n] == "M":
                result += 1000
                n += 1
                
            if n + 1 < x:
                if A[n:n+2] == "CM": 
                    result += 900
                    n += 2

            if n < x and  A[n] == "D":
                result += 500
                n += 1
                
            if n + 1 < x:
                if A[n:n+2] == "CD": 
                    result += 400
                    n += 2
                    
            if n < x and A[n] == "C":
                result += 100
                n += 1    
                
            if n + 1 < x:
                if A[n:n+2] == "XC": 
                    result += 90
                    n += 2  

            if n < x and A[n] == "L":
                result += 50
                n += 1  
                
            if n + 1 < x:
                if A[n:n+2] == "XL": 
                    result += 40
                    n += 2

            if n < x and A[n] == "X":
                result += 10
                n += 1  
                
            if n + 1 < x:
                if A[n:n+2] == "IX": 
                    result += 9
                    n += 2  
                    
            if n < x and A[n] == "V":
                result += 5
                n += 1              
            
            if n + 1 < x:
                if A[n:n+2] == "IV": 
                    result += 4
                    n += 2    
            
            if n < x and A[n] == "I":
                result += 1
                n += 1 
            
        return result
        
