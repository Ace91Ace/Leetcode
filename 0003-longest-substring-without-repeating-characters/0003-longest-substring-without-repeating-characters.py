class Solution:  
    def lengthOfLongestSubstring(self, s: str) -> int:  
        maxc = 0  
        sp = 0  
        fp = 0  
        cs= set()  

        while sp < len(s):  
            if s[sp] not in cs:  
                cs.add(s[sp])  
                maxc = max(maxc, sp - fp + 1)  
                sp += 1  
            else:  
                cs.remove(s[fp])  
                fp += 1  

        return maxc