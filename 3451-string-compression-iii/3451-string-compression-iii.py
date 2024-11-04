class Solution:  
    def compressedString(self, word: str) -> str:  
        curr = word[0]  
        l = 1  
        x = []  
        
        for i in range(1, len(word)):  
            if curr == word[i]:  
                l += 1  
            else:
                if l > 0:  
                    x.append(str(l))  
                    x.append(curr)  
                curr = word[i]  
                l = 1  
            
            if l == 9:  
                x.append(str(l))  
                x.append(curr)  
                l = 0   

        if l > 0:  
            x.append(str(l))  
            x.append(curr)  

        return ''.join(x)