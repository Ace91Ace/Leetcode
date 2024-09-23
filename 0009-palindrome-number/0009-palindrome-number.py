class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        #Base Case
        if len(s)==1 or len(s)==0:
            return True
        
        if s[0]==s[-1]:
            return self.isPalindrome(s[1:-1])
        return False