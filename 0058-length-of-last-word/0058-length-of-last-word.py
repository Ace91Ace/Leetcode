class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        st = s.strip()
        for i in range(len(st)-1,0,-1):
            if st[i] == " ":
                return count
            else:
                count+=1
        return count 
