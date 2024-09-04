class Solution:
    def reverseWords(self, s: str) -> str:
        re = s.split()
        re.reverse()
        return ' '.join(re)