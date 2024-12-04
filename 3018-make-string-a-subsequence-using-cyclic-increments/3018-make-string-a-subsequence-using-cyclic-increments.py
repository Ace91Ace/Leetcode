
class Solution:  
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        sta = list(str2)  
        top = 0  
        
        for i in range(len(str1)):  
            if top == len(sta):  
                return True  
            if str1[i] == sta[top] or ord(str1[i]) + 1 == ord(sta[top]) or (str1[i] == 'z' and sta[top] == 'a'):  
                top += 1  
        return top == len(sta) 