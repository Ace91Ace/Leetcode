class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        s1 = s1.split()
        s2 = s2.split()
        sx = set(s1)
        sy = set(s2)
        xs = (sx-sy).union(sy-sx)
        z = s1 + s2
        
        return [x for x in xs if z.count(x) == 1 ]