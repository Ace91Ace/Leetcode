class Solution:  
    def lengthOfLongestSubstring(self, s: str) -> int:  
        x = set()
        l = 0
        maxc = 0

        for r in range(len(s)):
            while s[r] in x:
                x.remove(s[l])
                l += 1
            x.add(s[r])

            maxc = max(maxc, r-l+1)
        return maxc