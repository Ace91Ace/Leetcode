class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        vis = []
        n = len(nums)
        ind = [i for i in range(n) if nums[i] == key]

        for i in ind:
            l = max(0, i-k)
            u = min(n-1, i+k)
            for j in range(l, u+1):
                if vis and j > vis[-1]:
                    vis.append(j)
                elif not vis:
                    vis.append(j)
        return vis