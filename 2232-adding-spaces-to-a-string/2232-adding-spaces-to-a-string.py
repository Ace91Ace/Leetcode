class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        j = 0
        for i in spaces:
            res += s[j:i] + " "
            j = i 
        res += s[spaces[-1]:]
        return res