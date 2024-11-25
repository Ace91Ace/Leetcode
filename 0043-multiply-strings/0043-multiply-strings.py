class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = n2 = 0
        
        num1 = num1[::-1]
        for i in range(len(num1)):
            n1 = n1 + (10**(i))*(ord(num1[i])-48)

        num2 = num2[::-1]
        for i in range(len(num2)):
            n2 = n2 + (10**(i))*(ord(num2[i])-48)
        
        return str(n1*n2)
        

