

class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
        
        dic = {"I": 1, "II": 2, 'III': 3, 'IV': 4, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D':500, 'M': 1000}
        
        result = ""

        if A >= 1000:
            
            x = A / 1000
            result +=  "M" * x
            
            A = A % 1000

        if A >= 900:
            
            x = A / 900
            result +=  "CM" * x
            
            A = A % 900
            
        if A >= 500:
    
            x = A / 500
            result +=  "D" * x
            
            A = A % 500

        if A >= 400:
    
            x = A / 400
            result +=  "CD" * x
            
            A = A % 400

        if A >= 100:
    
            x = A / 100
            result +=  "C" * x
            
            A = A % 100
            
        if A >= 90:
    
            x = A / 90
            result +=  "XC" * x
            
            A = A % 90
            
        if A >= 50:
    
            x = A / 50
            result +=  "L" * x
            
            A = A % 50

        if A >= 40:
    
            x = A / 40
            result +=  "XL" * x
            
            A = A % 40

        if A >= 10:
    
            x = A / 10
            result +=  "X" * x
            
            A = A % 10

        if A >= 9:
    
            x = A / 9
            result +=  "IX" * x
            
            A = A % 9
        
        if A >= 5:
    
            x = A / 5
            result +=  "V" * x
            
            A = A % 5

        if A >= 4:
    
            x = A / 4
            result +=  "IV" * x
            
            A = A % 4

        if A >= 1:
    
            x = A / 1
            result +=  "I" * x
            
            A = A % 1
        return result
