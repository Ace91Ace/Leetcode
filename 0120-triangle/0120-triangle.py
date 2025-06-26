class Solution:
    #def minimumTotal(self, tri: List[List[int]]) -> int:
    #    n = len(tri)
    #    @lru_cache(None)
    #    def help(i, j):
    #        if i == n-1:
    #            return tri[i][j]
    #        return tri[i][j] + min(help(i+1,j), help(i+1,j+1))
    #    return help(0,0)

    def minimumTotal(self, tri: List[List[int]]) -> int:
        n = len(tri)
        dp = [[-1]*len(tri[-1]) for _ in range(n)]
        dp[n-1] = tri[-1]
        for i in range(n-2, -1, -1):
            for j in range(len(tri[i])):
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + tri[i][j]
        return dp[0][0]
