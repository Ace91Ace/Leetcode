class Solution:
    def minimumTotal(self, tri: List[List[int]]) -> int:
        n = len(tri)
        @lru_cache(None)
        def help(i, j):
            if i == n-1:
                return tri[i][j]
            return tri[i][j] + min(help(i+1,j), help(i+1,j+1))
        return help(0,0)
