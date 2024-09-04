class Solution:
    def reverseWords(self, s: str) -> str:
        re = s.split()[::-1]
        return ' '.join(re)