class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 : return False
        k = sum(nums)//2
        n = len(nums)
        dp = {}
        def dfs(i, sm):
            if (i,sm) in dp:
                return dp[(i,sm)]
            if sm == k:
                return True
            if i == n or sm > k:
                return False
            dp[(i,sm)] = dfs(i+1, sm) or dfs(i+1, sm + nums[i])
            return dp[(i,sm)]
        return dfs(0, 0)
        