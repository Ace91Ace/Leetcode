class Solution:
    def minimumSteps(self, s: str) -> int:
        count = 0
        res = 0
        for i in s[::-1]:
            if i == "0":
                count += 1
            else:
                res += count
        
        return res