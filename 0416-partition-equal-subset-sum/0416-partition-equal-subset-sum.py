from functools import lru_cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        k = total // 2
        n = len(nums)

        @lru_cache(None)
        def dfs(i, sm):
            if sm == k:
                return True
            if sm > k or i == n:
                return False
            return dfs(i + 1, sm + nums[i]) or dfs(i + 1, sm)

        return dfs(0, 0)
