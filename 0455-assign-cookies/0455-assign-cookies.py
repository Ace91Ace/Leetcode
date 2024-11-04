class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        n = 0
        g.sort()
        s.sort()

        while len(s) > 0 and len(g) > 0:
            if s[0] >= g[0]:
                n += 1
                s.pop(0)
                g.pop(0)
            else:
                s.pop(0)
        return n