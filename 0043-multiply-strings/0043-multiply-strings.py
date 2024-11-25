class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dit = {'1':1 ,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0 }
        n1 = n2 = 0

        num1 = num1[::-1]
        for i in range(len(num1)):
            n1 = n1 + (10**(i))*dit[num1[i]]

        num2 = num2[::-1]
        for i in range(len(num2)):
            n2 = n2 + (10**(i))*dit[num2[i]]
        
        return str(n1*n2)
        

