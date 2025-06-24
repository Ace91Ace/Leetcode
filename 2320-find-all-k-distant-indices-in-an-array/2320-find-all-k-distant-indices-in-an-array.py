class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        vis = set()
        n = len(nums)
        ind = [i for i in range(n) if nums[i] == key]

        for i in ind:
            l = max(0, i-k)
            u = min(n-1, i+k)
            for j in range(l, u+1):
                vis.add(j)
        return sorted(vis)